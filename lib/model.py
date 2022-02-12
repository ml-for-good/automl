import autokeras as ak
import tensorflow as tf

REGRESSION = 'regression'
CLASSIFICATION = 'classification'

SAVED_MODEL = 'saved_model'
TFTRT = 'tftrt'
TFLITE = 'tflite'
ONNX = 'onnx'


class StructuredDataModel:
    """
      Work flow:
       ┌───────────────┐
       │ Make datasets │
       └───────┬───────┘
               │
       ┌───────▼───────┐
       │ Train model   │
       └───────┬───────┘
               │
       ┌───────▼────────┐
       │ Evaluate model │
       └───────┬────────┘
               │
      ┌────────▼──────────┐
      │ Export best model │
      └────────┬──────────┘
               │
        ┌──────▼────────┐          ▼
        │ Serving model │
        └───────────────┘
      Train model from structured data, it will tune hparams automatically and do some nas searches, it will record training logs in a csv file.
      Args:
        max_trials: Int. The maximum number of different Keras Models to try.
          The search may finish before reaching the max_trials.
        task: task type.
    """

    def __init__(self, max_trials, task):
        if task == REGRESSION:
            self.model = ak.StructuredDataRegressor(max_trials=max_trials)
        elif task == CLASSIFICATION:
            self.model = ak.StructuredDataClassifier(max_trials=max_trials)

        else:
            raise NotImplemented
        self.callbacks = [
            tf.keras.callbacks.CSVLogger(
                tf.io.gfile.join(self.model.directory, 'training_log.csv')),
            tf.keras.callbacks.ProgbarLogger()
        ]

    def train(self, dataset, batch_size=8, epochs=10):
        """
          Args:
            dataset: Train dataset, tf dataset format.
            batch_size: Train batch size, integer.
            epochs: Train loops, integer.
        """
        return self.model.fit(dataset,
                              epochs=epochs,
                              batch_size=batch_size,
                              callbacks=self.callbacks)

    def evaluate(self, dataset):
        return self.model.evaluate(dataset)

    def export(self, format=SAVED_MODEL):
        if format==SAVED_MODEL:
          model = self.model.export_model()
          tf.saved_model.save(model, tf.io.gfile.join(self.model.directory, 'saved_model'))
        else:
          raise NotImplemented


class TextModel:
    pass


class ImageModel:
    pass
