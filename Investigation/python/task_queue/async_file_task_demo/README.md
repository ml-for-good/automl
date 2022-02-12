## 启动流程
1. `minikube stop && minikube start --memory 3000 --insecure-registry localhost:5000`
2. (首次启动运行)`minikube addons enable heapster`
3. `eval $(minikube docker-env)`
4. `cd api_async_upload && docker build . -t async-upload`
5. `cd celery_worker && docker build . -t celery-worker`
6. `kubectl create -f cluster_builder/rabbitmq/rabbitmq-controller.yaml`
7. `kubectl create -f cluster_builder/rabbitmq/rabbitmq-service.yaml`
8. `kubectl create -f cluster_builder/flower/flower-controller.yaml`
9. `kubectl create -f cluster_builder/flower/flower-service.yaml`
10. `kubectl create -f cluster_builder/celery/celery-deployment.yaml`
11. `kubectl create -f cluster_builder/api_server/api-server-deployment.yaml`
13. `kubectl create -f cluster_builder/hpa.yaml`



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



## 数据可视化

1. k8s集群信息 `minikube dashboard --url`
2. celery监控信息 `kubectl port-forward svc/flower-service 5555:5555`, 其中`flower-service`是之前创建的service, 这里用 port-forward进行端口转发, 可以在本地访问集群的应用
3. rabbit mq 监控信息 `kubectl port-forward pod/rabbitmq-controller-4n5wh 15672:15672`, 同上, rabbit mq 如果需要登录, user_name:guest, password:guest



## log 查看

进入k8s集群可视化页面, 在首页pods最后的展开有logs, 访问每个pod的log信息



## hpa 伸缩
`kubectl autoscale deployment worker-controller --cpu-percent=50 --min=1 --max=10`, 其中 `worker-controller` 是之前启动的deploment(autoscaling 作用于 Replication Controller 对象), 例如现在有一个pod, 但是该pod的cpu利用率>50, 伸展为2个pod, 如果两个pod的cpu平均利用率>50, 伸展为3个, 缩减同理.
`kubectl get hpa`或者`watch -d -n 0.5 kubectl get hpa`

### 参考文档
1. [什么是ReplicationController](什么是ReplicationController)
2. [什么是k8s的label?](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/)
3. [k8s中metadata.labels和template.metadata.labels有什么区别吗?](https://www.zhihu.com/question/473339868/answer/2010187411)
4. [yaml文件基础语法](https://www.cnblogs.com/wn1m/p/11286109.html)
5. [什么是 spec](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/)
5. [什么是 spec的selector](https://www.cnblogs.com/freeaihub/p/12967117.html)
6. [service yaml文件的功能](https://www.cnblogs.com/freeaihub/p/12967117.html)
7. [service types 的区别](https://blog.csdn.net/weixin_40274679/article/details/107887678)
8. [service types 的区别2](https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types)
9. [参考项目](https://github.com/pangyuteng/k8s-celery-autoscale)

