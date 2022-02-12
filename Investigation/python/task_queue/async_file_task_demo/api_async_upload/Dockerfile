FROM python:3.6.6

WORKDIR /api_server
COPY . .

RUN pip install --user --upgrade pip
RUN python -m pip install --user -r requirements.txt

ENV C_FORCE_ROOT 1

CMD ["python3", "app.py"]
