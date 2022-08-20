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

再开始部署前,确保部署文件为最新!!!

在``automl/deploy``目录下开始执行部署

#### Step 1: 部署依赖服务

**MySQL部署**

创建MySQL的**namespace**:

```
kubectl create ns mysql
```

部署MySQL：

```
# No.1
kubectl apply -f mysql-pv.yaml
# No.2
kubectl apply -f mysql-pvc.yaml
# No.3
kubectl apply -f mysql-deployment.yaml
```

**Minio部署**

创建Minio的**namespace**:

```bash
kubectl create ns minio
```

部署Minio：

```bash
kubectl apply -f minio-deployment.yaml
```

**Kafka部署**

Todo

**Redis部署**

Todo

...

#### Step 2: 部署AutoML平台:

创建AutoML的**namespace:**

```
kubectl create ns automl
```

部署AutoML：

```bash
kubectl apply -f automl-deployment.yaml
```

## License

Todo
