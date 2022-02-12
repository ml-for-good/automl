import os

from celery import Celery
from flask import Flask, jsonify, request
from flask_cors import CORS
from minio import Minio
from werkzeug.utils import secure_filename


data_volume_path = "/data"
broker_service_host = os.environ.get('RABBITMQ_SERVICE_SERVICE_HOST')
broker_url = f"amqp://guest:guest@{ broker_service_host }:5672//"

app = Flask(__name__)
CORS(app,  resources={r"/*": {"origins": "*"}})

app.config['CELERY_BROKER_URL'] = broker_url
app.config['CELERY_RESULT_BACKEND'] = broker_url

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)
print(f"Authorized broker url: { format(celery.conf.broker_url) } ")


@app.route("/")
def index():
    api_root = {
        "versions": {
            "values": [
                {
                    "id": "v0",
                    "links": [{"href": "v0/", "rel": "self"}],
                    "media-types": [
                        {
                            "base": "application/json",
                            "type": "application/vnd.automl.api-v0 json",
                        }
                    ],
                    "status": "dev",
                    "updated": "2022-02-12T00:00:00Z",
                }
            ]
        }
    }
    return jsonify(api_root)


@app.route("/upload_async", methods=["POST"])
def upload_file():
    file = request.files['file']
    filename = secure_filename(file.filename)
    filepath = os.path.join(data_volume_path, filename)
    file.save(filepath)
    upload_oss.apply_async(args=(filepath, filename))
    return jsonify(filepath=filepath, filename=filename)


@celery.task
def upload_oss(file_path, file_name):
    # Using internet minio playground: play.min.io
    oss_client = Minio(
        "play.min.io",
        access_key="Q3AM3UQ867SPQQA43P2F",
        secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
    )
    bucket_name = "ml4good"  # hardcoded for poc

    found = oss_client.bucket_exists(bucket_name)
    if not found:
        oss_client.make_bucket(bucket_name)
    else:
        print(f"Bucket '{ bucket_name }' already exists")

    # file_path as object name for poc only
    oss_client.fput_object(
        bucket_name, file_name, file_path,
    )
    print(
        f"'{ file_path }' is successfully uploaded as "
        f"object '{ file_name }' to bucket ' { bucket_name }'. "
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8040, debug=True)
