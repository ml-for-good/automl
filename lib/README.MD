##Quick start
```
pip install -r requirements.txt && python lib/data_test.py
```

##Format
```
yapf --style=google -i lib/*.py
```

## Docker
```
docker build .
```

## Usage
```python
from lib import data
from lib import model

train_data_url = "train csv file path"
test_data_url = "test csv file path"

train_dataset, test_dataset = data.Dataloader.from_csv(
    train_data_url,
    test_data_url,
    label_name='survived',
    cache_dir=None,
    batch_size=2)

clf = model.StructuredDataModel(3, model.CLASSIFICATION)

clf.train(train_dataset)
clf.evaluate(test_dataset)
```
