from lib import data
from lib import model
from absl import app
from absl import logging
from absl import flags
import tensorflow as tf

flags.DEFINE_bool('profile', False, 'Profile performance.')

FLAGS = flags.FLAGS


def main(_):
    train_data_url = "https://storage.googleapis.com/tf-datasets/titanic/train.csv"
    test_data_url = "https://storage.googleapis.com/tf-datasets/titanic/eval.csv"
    logging.info('Load CSV dataset')
    if FLAGS.profile:
      tf.profiler.experimental.start('./profile')
    train_dataset, test_dataset = data.Dataloader.from_csv(
        train_data_url,
        test_data_url,
        label_name='survived',
        cache_dir=None,
        batch_size=2)
    logging.info('Build a classifier model')
    clf = model.StructuredDataModel(3, model.CLASSIFICATION)
    logging.info('Start training')
    clf.train(
        # Take top 100 samples for training test
        train_dataset.take(100),
        batch_size=2,
        epochs=10,
    )
    if FLAGS.profile:
      tf.profiler.experimental.stop()
    logging.info('Start evaluating')
    # Take top 100 samples for evaluate test
    clf.evaluate(test_dataset.take(100))


if __name__ == "__main__":
    app.run(main)
