from flask import Flask
from flask import request

import uuid
from datetime import datetime
import tensorflow as tf

from tflite_model_maker.config import ExportFormat
from tflite_model_maker import model_spec
from tflite_model_maker import object_detector
from tflite_model_maker import text_classifier

app = Flask('automl')


class Task:
    task_id = None
    model = None
    status = None
    start_time = None
    end_time = None
    error = None


class TaskManager:
    tasks = {}

    def init(self):
        task = Task()
        task.task_id = str(uuid.uuid1())
        task.start_time = datetime.utcnow()
        task.status = 'start'
        self.tasks[task.task_id] = task
        return task

    def get(self, task_id):
        return self.tasks.get(task_id, None)

    def delete(self, task_id):
        del self.tasks[task_id]


def create_detection_service():
    manager = TaskManager()
    spec = model_spec.get('efficientdet_lite0')

    @app.route('/v1/detection/init', methods=['GET', 'POST'])
    def init():
        return {'task_id': manager.init().task_id, 'msg': 'Init success'}

    @app.route('/v1/detection/train', methods=['POST'])
    def train():
        train_dataset = request.form['train_dataset']
        test_dataset = request.form['test_dataset']
        batch_size = int(request.form['batch_size'])
        epochs = int(request.form['epochs'])
        task_id = request.form['task_id']
        task = manager.get(task_id)
        if task is None:
            return {'msg': 'Task is not found'}
        if train_dataset.endswith('csv') and test_dataset.endswith('csv'):
            task.status = 'downloading dataset'
            train_data, validation_data, _ = object_detector.DataLoader.from_csv(
                train_dataset)
            _, _, test_data = object_detector.DataLoader.from_csv(test_dataset)
            task.status = 'training'
            task.model = object_detector.create(train_data,
                                                model_spec=spec,
                                                batch_size=batch_size,
                                                validation_data=validation_data,
                                                epochs=epochs)
            task.status = 'evaluating'
            metric = task.model.evaluate(test_data)
            task.status = 'free'
            return {'msg': 'Train finished', 'metric': metric}
        else:
            return {'msg': 'Service is not implemented'}

    @app.route('/v1/detection/predict', methods=['POST'])
    def predict():
        task_id = request.form['task_id']
        image_url = request.form['image_url']
        task = manager.get(task_id)
        if task is None:
            return {'msg': 'Task is not found'}
        content = tf.io.read_file(image_url)
        image = tf.io.decode_image(content)
        result = task.model.model([image])
        return {'msg': 'predict success', 'result': result}

    @app.route('/v1/detection/view', methods=['GET'])
    def view():
        tasks = {}
        for task_id, task in manager.tasks.items():
            tasks[task_id] = {'start_time': task.start_time}
            tasks[task_id] = {'end_time': task.end_time}
            tasks[task_id] = {'status': task.status}
        return {
            'msg': 'Current tasks' + str(len(manager.tasks)),
            'tasks': tasks
        }

    @app.route('/v1/detection/export', methods=['POST'])
    def export():
        task_id = request.form['task_id']
        url = request.form['url']
        task = manager.get(task_id)
        if task is None:
            return {'msg': 'Task is not found'}
        task.status = 'exporting'
        task.model.export(
            export_dir=url,
            export_format=[ExportFormat.SAVED_MODEL, ExportFormat.LABEL])
        task.status = 'free'
        return {'msg': 'Model exported success'}

    @app.route('/v1/detection/delete/<task_id>', methods=['DELETE'])
    def delete(task_id):
        task = manager.get(task_id)
        manager.delete(task_id)
        task.status = 'deleted'
        return {'msg': 'Task was deleted'}


def create_nlp_service():
    manager = TaskManager()
    spec = model_spec.get('average_word_vec')

    @app.route('/v1/nlp/init', methods=['GET', 'POST'])
    def init():
        return {'task_id': manager.init().task_id, 'msg': 'Init success'}

    @app.route('/v1/nlp/train', methods=['POST'])
    def train():
        train_dataset = request.form['train_dataset']
        test_dataset = request.form['test_dataset']
        batch_size = int(request.form['batch_size'])
        epochs = int(request.form['epochs'])
        task_id = request.form['task_id']
        task = manager.get(task_id)
        if task is None:
            return {'msg': 'Task is not found'}
        if train_dataset.endswith('csv') and test_dataset.endswith('csv'):
            task.status = 'training'
            train_data = text_classifier.DataLoader.from_csv(
                train_dataset,
                is_training=True,
                text_column='sentence',
                label_column='label',
                model_spec=spec)
            test_data = text_classifier.DataLoader.from_csv(
                test_dataset,
                is_training=False,
                text_column='sentence',
                label_column='label',
                model_spec=spec)
            task.model = text_classifier.create(train_data,
                                                model_spec=spec,
                                                batch_size=batch_size,
                                                epochs=epochs)
            task.status = 'evaluating'
            metric = task.model.evaluate(test_data)
            return {'msg': 'Train finished', 'metric': metric}
        else:
            return {'msg': 'Service is not implemented'}

    @app.route('/v1/nlp/predict', methods=['POST'])
    def predict():
        task_id = request.form['task_id']
        sentence = request.form['sentence']
        task = manager.get(task_id)
        if task is None:
            return {'msg': 'Task is not found'}
        result = task.model.model([sentence])
        return {'msg': 'predict success', 'result': result}

    @app.route('/v1/nlp/view', methods=['GET'])
    def view():
        tasks = {}
        for task_id, task in manager.tasks.items():
            tasks[task_id] = {'start_time': task.start_time}
            tasks[task_id] = {'end_time': task.end_time}
            tasks[task_id] = {'status': task.status}
        return {
            'msg': 'Current tasks' + str(len(manager.tasks)),
            'tasks': tasks
        }

    @app.route('/v1/nlp/export', methods=['POST'])
    def export():
        task_id = request.form['task_id']
        url = request.form['url']
        task = manager.get(task_id)
        if task is None:
            return {'msg': 'Task is not found'}
        task.model.export(
            export_dir=url,
            export_format=[ExportFormat.SAVED_MODEL, ExportFormat.LABEL])
        return {'msg': 'Model exported success'}

    @app.route('/v1/nlp/delete/<task_id>', methods=['DELETE'])
    def delete(task_id):
        manager.delete(task_id)
        return {'msg': 'Task was deleted'}


create_detection_service()
# create_nlp_service()
