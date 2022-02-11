from lib import data
from lib import model
from absl import app
from absl import logging


def main(_):
    train_data_url = "https://storage.googleapis.com/tf-datasets/titanic/train.csv"
    test_data_url = "https://storage.googleapis.com/tf-datasets/titanic/eval.csv"
    logging.info('Load dataset')
    train_dataset, test_dataset = data.Dataloader.from_csv(
        train_data_url,
        test_data_url,
        label_name='survived',
        cache_dir=None,
        batch_size=2)
    logging.info('Start training')
    clf = model.StructuredDataModel(3, model.CLASSIFICATION)
    clf.train(
        train_dataset.take(100),
        batch_size=2,
        epochs=10,
    )
    logging.info('Start evaluating')
    clf.evaluate(test_dataset.take(100))


if __name__ == "__main__":
    app.run(main)
