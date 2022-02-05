import tensorflow as tf
import tensorflow_io as tfio
import autokeras as ak
import data

class DataloaderTest(tf.test.TestCase):
    def test_csv(self):
        TRAIN_DATA_URL = "https://storage.googleapis.com/tf-datasets/titanic/train.csv"
        TEST_DATA_URL = "https://storage.googleapis.com/tf-datasets/titanic/eval.csv"

        train_dataset, test_dataset = data.DataLoader.from_csv(TRAIN_DATA_URL, TEST_DATA_URL, label_name='survived', cache_dir=None)
        clf = ak.StructuredDataClassifier(
            overwrite=True, max_trials=3
        )
        clf.fit(
            train_dataset,
            epochs=10,
            callbacks=[tf.keras.callbacks.TensorBoard()],
        )
        clf.evaluate(test_dataset)
