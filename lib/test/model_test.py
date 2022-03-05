import tensorflow as tf
from lib import model


class DataloaderTest(tf.test.TestCase):

    def test_train(self):
        reg = model.StructuredDataModel(1, model.REGRESSION)
        clf = model.StructuredDataModel(1, model.CLASSIFICATION)
