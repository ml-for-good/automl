# AutoML

We're designing the AutoML platform that would make it easy for non-technical people to build custom AI solutions and
AI-powered process automation.

Easy-to-use ML platforms leverage the time/value/knowledge trade-off in a genuinely attractive way and allow users with
no AI coding skills to optimize day-to-day operations and to solve business issues.

## API

API Link: Todo

## How Minikube deploys AutoML

AutoML的部署脚本维护在``./deploy``目录下.
按照以下指南在你本地Minikube上部署AutoML平台.

### Prerequisites

开始之前,请确保一下组件安装在你的机器上:

- Docker
- Minikube

安装教程:

**Mac OS:**

- Docker: https://docs.docker.com/desktop/install/mac-install/

- Minikube: ``brew install minikube``
  - 详细参考:https://minikube.sigs.k8s.io/docs/start/

**Linux:** Todo

**Windows:** Todo

### Start Deploy

开始部署前,确保启动minikube和获取最新部署文件!!!

启动Minikube: https://minikube.sigs.k8s.io/docs/drivers/docker/

```bash
minikube start --driver=docker #使用 docker 驱动启动集群
```

在``automl``目录下执行命令:

```bash
kubectl apply -f deploy
```

查看pod,svc,deployment信息:

```bash
kubectl get pod,svc,deployment,pv,pvc -n mysql
```

### 测试连接

获取 minikube的 `IP` 和service的`NodePort`

```bash
minikube service mysql -n mysql --url
```

使用本地Navicat客户端连接数据库,连接信息:

``Host:IP``

``port:NodePort``

``用户名:root``

``密码:root``

## License

Todo
