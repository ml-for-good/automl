import tensorflow as tf
import tensorflow_io as tfio
import multiprocessing

IMAGE = 'image'
TEXT = 'text'


class Dataloader:

    @staticmethod
    def _decode_image(feat, image_size):
        """Decode image from jpeg, png, bmp, gif, webp"""
        if tf.strings.regex_full_match(feat, '.*(\.jpe?g|\.png|\.bmp)$'):
            contents = tf.io.read_file(feat)
            images = tf.image.decode_image(contents,
                                           channels=3,
                                           expand_animations=False)
            feat = tf.image.resize(images, image_size)
        elif tf.strings.regex_full_match(feat, '.*\.gif$'):
            contents = tf.io.read_file(feat)
            images = tf.image.decode_gif(contents)
            feat = tf.image.resize(images, image_size)
        elif tf.strings.regex_full_match(feat, '.*\.webp$'):
            contents = tf.io.read_file(feat)
            images = tfio.image.decode_webp(contents)
            feat = tf.image.resize(images, image_size)
        else:
            feat = tf.zeros(image_size, dtype=tf.uint8)
        return feat

    @classmethod
    def _text_map_fn(cls, feature, label):
        """Cast all csv values to string format"""
        result = []
        for feat in feature.values():
            if feat.dtype != tf.string:
                feat = tf.as_string(feat)
            result.append(feat)
        return tf.transpose(result), label

    @classmethod
    def _image_map_fn(cls, feature, label, image_size):
        result = []
        for feat in feature.values():
            feat = tf.map_fn(lambda f: cls._decode_image(f, image_size),
                             feat,
                             fn_output_signature=tf.string)
            result.append(feat)
        return tf.transpose(result), label

    @classmethod
    def from_csv(cls,
                 train_file_pattern,
                 val_file_pattern,
                 feature_columns=None,
                 label_name=None,
                 delimiter=',',
                 cache_dir='/tmp/automl',
                 batch_size=8,
                 task=TEXT):
        """ Get tensorflow datasets from csv files.
        Args:
          train_file_pattern: Train csv file pattern.
          val_file_pattern: Test csv file pattern.
          feature_columns: Dict specific selected columns and default values.
          label_name: An optional string corresponding to the label column. If
              provided, the data for this column is returned as a separate `Tensor` from
              the features dictionary, so that the dataset complies with the format
              expected by a `tf.Estimator.train` or `tf.Estimator.evaluate` input
              function.
          delimiter: An optional `string`. Defaults to `","`. Char delimiter to
              separate fields in a record.
          cache_dir: Dataset cache directory.
          batch_size: Train batch size.
        """
        if feature_columns:
            select_cols = list(feature_columns.keys())
            column_defaults = list(feature_columns.values())
        else:
            select_cols = None
            column_defaults = None

        def _get_dataset(file_pattern, shuffle=True):
            dataset = tf.data.experimental.make_csv_dataset(
                file_pattern,
                batch_size,
                shuffle=shuffle,
                num_parallel_reads=multiprocessing.cpu_count() // 2,
                label_name=label_name,
                column_defaults=column_defaults,
                field_delim=delimiter,
                select_columns=select_cols,
                prefetch_buffer_size=64,
                ignore_errors=True)
            # cache dataset in a directory
            if cache_dir:
                dataset = dataset.cache(cache_dir)
            if task == TEXT:
                map_fn = cls._text_map_fn
            elif task == IMAGE:
                map_fn = cls._image_map_fn
            else:
                raise NotImplemented
            # Set dataset optimize options
            options = tf.data.Options()
            options.experimental_optimization.map_parallelization = True
            options.experimental_optimization.parallel_batch = True
            return dataset.map(map_fn,
                               num_parallel_calls=multiprocessing.cpu_count()
                              ).unbatch().with_options(options)

        train_dataset = _get_dataset(train_file_pattern)
        val_dataset = _get_dataset(val_file_pattern, False)
        return train_dataset, val_dataset

    def from_folder(self):
        pass
