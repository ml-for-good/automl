import requests

proxies = {
    "http": None,
    "https": None,
}

res = requests.get('http://127.0.0.1:5000/v1/detection/init',
                   proxies=proxies).json()
task_id = res.get('task_id', None)
print(task_id)
res = requests.get('http://127.0.0.1:5000/v1/detection/view',
                   proxies=proxies).json()
print(res.get('tasks', None))
res = requests.post(
    'http://127.0.0.1:5000/v1/detection/train',
    proxies=proxies,
    data={
        'task_id':
            task_id,
        'train_dataset':
            'gs://cloud-ml-data/img/openimage/csv/salads_ml_use.csv',
        'test_dataset':
            'gs://cloud-ml-data/img/openimage/csv/salads_ml_use.csv',
        'batch_size':
            8,
        'epochs':
            10
    })
if res.status_code != 200:
    print(res.json().get('msg', None))
# res = requests.post('http://127.0.0.1:5000/v1/detection/predict', proxies=proxies, data={'task_id': task_id, 'url': 'gs://cloud-ml-data/img/openimage/csv/salads_ml_use.csv', 'batch_size':8})
