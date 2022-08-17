

# AutoML

We're designing the AutoML platform that would make it easy for non-technical people to build custom AI solutions and
AI-powered process automation.

Easy-to-use ML platforms leverage the time/value/knowledge trade-off in a genuinely attractive way and allow users with
no AI coding skills to optimize day-to-day operations and to solve business issues.

## API

API Link: Todo

## How Minikube deploys AutoML

按照一下指南在您本地Minikube上部署AutoML.

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

#### Step 1: 部署依赖服务

**MySQL部署**

创建MySql的**namespace**:

```
kubectl create ns mysql
```

获取Deployment：[mysql-deployment.yaml](https://github.com/ml-for-good/automl/tree/main/Investigation/mysql/deploy)

部署MySQL：

```
kubectl apply -f mysql-deployment.yaml
```

**Minio部署**

创建Minio的**namespace**:

```bash
kubectl create ns minio
```

获取Deployment：[minio-deployment.yaml](https://github.com/ml-for-good/automl/blob/main/Investigation/minio/deploy.yml)

部署Minio：

```bash
kubectl apply -f minio-deployment.yaml
```

**Kafka部署**

**Redis部署**

...

#### Step 2: 部署AutoML平台:

创建AutoML的**namespace:**

```
kubectl create ns automl
```

获取Deployment：[automl-deployment.yaml](https://github.com/ml-for-good/automl/blob/main/Investigation/java/deploy/deployment.yaml)

部署AutoML：

```bash
kubectl apply -f automl-deployment.yaml
```

## License

Todo
