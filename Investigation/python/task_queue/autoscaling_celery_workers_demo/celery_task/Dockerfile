FROM python:3.6.6

WORKDIR /celery_task_wp
COPY . .

RUN pip install --user --upgrade pip
RUN python -m pip install --user -r requirements.txt

ENV C_FORCE_ROOT 1

CMD ["/bin/bash", "run_task.sh"]

