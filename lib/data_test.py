import tensorflow as tf
import data


class DataloaderTest(tf.test.TestCase):

    def test_csv(self):
        train_data_url = "https://storage.googleapis.com/tf-datasets/titanic/train.csv"
        test_data_url = "https://storage.googleapis.com/tf-datasets/titanic/eval.csv"
        specs = (tf.TensorSpec(shape=(8, 9), dtype=tf.string),
                 tf.TensorSpec(shape=(8,), dtype=tf.int32))
        train_dataset, test_dataset = data.Dataloader.from_csv(
            train_data_url,
            test_data_url,
            label_name='survived',
            cache_dir=None)
        tf.nest.map_structure(
            lambda spec, target: self.assertTrue(spec.is_compatible_with(
                target)), train_dataset.element_spec, specs)
        tf.nest.map_structure(
            lambda spec, target: self.assertTrue(spec.is_compatible_with(
                target)), test_dataset.element_spec, specs)
