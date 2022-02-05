import tensorflow as tf
import multiprocessing


class DataLoader:
    @staticmethod
    def from_csv(train_file_pattern, val_file_pattern, feature_columns=None, label_name=None, delimiter=',', cache_dir='/tmp/automl', batch_size=8):
        if feature_columns:
            select_cols = list(feature_columns.keys())
            column_defaults = list(feature_columns.values())
        else:
            select_cols=None
            column_defaults=None
        def _get_dataset(file_pattern, shuffle=True):
            filenames = tf.io.gfile.glob(file_pattern)
            dataset = None
            for filename in filenames:
                with tf.io.gfile.GFile(filename, 'rb') as file:
                    new_dataset = tf.data.experimental.make_csv_dataset(filename, batch_size, shuffle=shuffle, num_parallel_reads=multiprocessing.cpu_count()//2,
                                                                        label_name=label_name, column_defaults=column_defaults,
                                                                        field_delim=delimiter, select_columns=select_cols, ignore_errors=True)
                    if isinstance(dataset, tf.data.Dataset):
                        dataset = dataset.concatenate(new_dataset)
                    elif dataset is None:
                        dataset = new_dataset

            def _map_fn(feature, label):
                result = []
                for feat in feature.values():
                    if feat.dtype!=tf.string:
                        result.append(tf.as_string(feat))
                    else:
                        result.append(feat)
                return tf.transpose(result), label
            if cache_dir:
                dataset = dataset.cache(cache_dir)
            return dataset.map(_map_fn)

        train_dataset = _get_dataset(train_file_pattern)  
        val_dataset = _get_dataset(val_file_pattern, False)
        return train_dataset, val_dataset
    
    def from_folder(self):
        pass