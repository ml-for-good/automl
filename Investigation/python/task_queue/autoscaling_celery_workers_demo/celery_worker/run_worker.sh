#!/bin/bash

python3 -m celery -A config worker -c 1 -b amqp://guest:guest@$RABBITMQ_SERVICE_SERVICE_HOST:5672