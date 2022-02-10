import os
from celery import Celery


class CeleryConfig:
    broker_service_host = os.environ.get('RABBITMQ_SERVICE_SERVICE_HOST')
    # broker变量配置: https://docs.celeryproject.org/en/stable/userguide/configuration.html#broker-settings
    broker_url = 'amqp://guest:guest@{}:5672//'.format(broker_service_host)
    celery_broker_url = broker_url
    celery_broker_url
    print("broker url:{}".format(celery_broker_url))

app = Celery('tasks')
app.config_from_object(CeleryConfig)
print('authorize broker url: {} '.format(app.conf.broker_url))

@app.task
def add(a, b):
    print("a:{:d}, b:{:d}".format(a, b))
    return a + b