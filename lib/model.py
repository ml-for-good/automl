import autokeras as ak
import tensorflow as tf

REGRESSION = 'regression'
CLASSIFICATION = 'classification'


class StructuredDataModel:
    """
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

    def train(self, dataset, epochs=10):
        return self.model.fit(
            dataset,
            epochs=epochs,
            callbacks=[tf.keras.callbacks.CSVLogger(self.model.directory)])

    def evaluate(self, dataset):
        return self.model.evaluate(dataset)


class TextModel:
    pass


class ImageModel:
    pass
