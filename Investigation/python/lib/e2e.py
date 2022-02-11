from lib import data
from lib import model


def main():
    train_data_url = "https://storage.googleapis.com/tf-datasets/titanic/train.csv"
    test_data_url = "https://storage.googleapis.com/tf-datasets/titanic/eval.csv"

    train_dataset, test_dataset = data.Dataloader.from_csv(
        train_data_url, test_data_url, label_name='survived', cache_dir=None)

    clf = model.StructuredDataModel(3, model.CLASSIFICATION)
    clf.train(
        train_dataset,
        epochs=10,
    )
    clf.evaluate(test_dataset)


if __name__ == "__main__":
    main()
