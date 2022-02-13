import random
import time

from config import add, CeleryConfig


while True:
    a = random.randint(1, 50)
    b = random.randint(50, 100)
    print("start time:{}".format(time.time()))
    add.apply_async(args=(a, b))
    print("end time:{} \n mq url:{}".format(time.time(), CeleryConfig.celery_broker_url))