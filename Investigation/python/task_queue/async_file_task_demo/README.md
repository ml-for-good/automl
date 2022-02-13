> This PoC is based on the auto scaling fork(a great job), just to enable a file upload to be asyc done via the celery worker, where a shared data volume was used.

```

   POST /upload_as
   -F "file=@test.txt"
                        │
                        │
                        │
                        │
                        │
  WSGI (flask)          │
 ┌──────────────────────▼────────────────────────────────────┐                ┌──────────────┐
 │@app.route("/upload_async", methods=["POST"])              │                │ Shared       │
 │def upload_file():                                         │                │ Volume       │
 │    file = request.files['file']                           │                │              │
 │    filename = secure_filename(file.filename)              │                │              │
 │    filepath = os.path.join(data_volume_path, filename)    │                │              │
 │    file.save(filepath)────────────────────────────────────┼────────────────►              │
 │                                                           │                │              │
 │    upload_oss.apply_async(args=(filepath, filename))──────┼─┐              │              │
 │    return jsonify(filepath=filepath, filename=filename)   │ │              │              │
 │                                                           │ │              │              │
 └───────────────────────────────────────────────────────────┘ │              │              │
                                                               │              │              │
  Message Bus(rabbit)                                          │              │              │
 ┌─────────────────────────────────────────────────────────────▼──────────┐   │              │
 │                                                                        │   │              │
 │                                                                        │   │              │
 └─────────────────────────────┬──────────────────────────────────────────┘   │              │
                               │                                              │              │
  WORKER (celery)              │                                              │              │
 ┌─────────────────────────────▼─────────────────────────────────┐      ┌─────┤              │
 │@celery.task                                                   │      │     │              │
 │def upload_oss(file_path, file_name):                          │      │     │              │
 │    # Using internet minio playground: play.min.io             │      │     │              │
 │    oss_client = Minio(                                        │      │     └──────────────┘
 │        "play.min.io",                                         │      │
 │        access_key="Q3AM3UQ867SPQQA43P2F",                     │      │     ┌──────────────┐
 │        secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG", │      │     │ OSS(MinIO)   │
 │    )                                                          │      │     │              │
 │    bucket_name = "ml4good"  # hardcoded for poc               │      │     │              │
 │                                                               │      │     │              │
 │    found = oss_client.bucket_exists(bucket_name)              │      │     │              │
 │    if not found:                                              │      │     │              │
 │        oss_client.make_bucket(bucket_name)                    │      │     │              │
 │    else:                                                      │      │     │              │
 │        print(f"Bucket '{ bucket_name }' already exists")      │      │     │              │
 │                                                               │      │     │              │
 │    # file_path as object name for poc only                    │      │     │              │
 │    oss_client.fput_object(                                    ├──────┴─────►              │
 │        bucket_name, file_name, file_path,                     │            │              │
 │    )                                                          │            │              │
 └───────────────────────────────────────────────────────────────┘            └──────────────┘
```

## 启动流程

```bash
minikube stop && minikube start --memory 3000 --insecure-registry localhost:5000
minikube addons enable heapster
eval $(minikube docker-env)
cd api_async_upload && docker build . -t async-upload
cd celery_worker && docker build . -t celery-worker
kubectl create -f cluster_builder/rabbitmq/rabbitmq-controller.yaml
kubectl create -f cluster_builder/rabbitmq/rabbitmq-service.yaml
kubectl create -f cluster_builder/celery/celery-deployment.yaml
kubectl create -f cluster_builder/api_server/api-server-deployment.yaml
```


## 测试

先让本机能访问 sync-upload 的 nodeport service：

```bash
$ minikube service --url async-upload-np-service

🏃  Starting tunnel for service async-upload-np-service.
|-----------|-------------------------|-------------|------------------------|
| NAMESPACE |          NAME           | TARGET PORT |          URL           |
|-----------|-------------------------|-------------|------------------------|
| default   | async-upload-np-service |             | http://127.0.0.1:50588 |
|-----------|-------------------------|-------------|------------------------|
http://127.0.0.1:50588
```

弄一个文件上传试试：

```bash
$ touch $HOME/Downloads/test.txt
$ echo hi > $HOME/Downloads/test.txt
$ curl http://127.0.0.1:50588/upload_async -F "file=@$HOME/Downloads/test.txt"
{
  "filename": "test.txt",
  "filepath": "/data/test.txt"
}
```



然后可以去公共的 minio 试玩地址，文件被传上去了：https://play.min.io:9443/buckets/ml4good/browse

- 账户密码
  - `Q3AM3UQ867SPQQA43P2F`
  - `tfteSlswRu7BJ86wekitnifILbZam1KYY3TG`
- 参考：https://docs.min.io/docs/python-client-quickstart-guide.html


