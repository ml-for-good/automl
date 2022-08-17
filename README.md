# AutoML

We're designing the AutoML platform that would make it easy for non-technical people to build custom AI solutions and
AI-powered process automation.

Easy-to-use ML platforms leverage the time/value/knowledge trade-off in a genuinely attractive way and allow users with
no AI coding skills to optimize day-to-day operations and to solve business issues.

## API

API Link: Todo

## Quick Start：

## How kubernetes deploys AutoML

部署之前需要开发一下端口：Todo

## Step 1: 部署依赖环境

- Minikube
- Docker

## Step 2:部署依赖服务:

获取Deployment：

Mysql:[https://github.com/ml-for-good/automl/tree/main/Investigation/mysql/deploy](https://github.com/ml-for-good/automl/tree/main/Investigation/mysql/deploy)
- Kafka:Todo
- Redis:Todo
-
Minio:[https://github.com/ml-for-good/automl/blob/main/Investigation/minio/deploy.yml](https://github.com/ml-for-good/automl/blob/main/Investigation/minio/deploy.yml)
- ….

## Step 3:部署AutoML

获取Deployment：

AutoML:[https://github.com/ml-for-good/automl/blob/main/Investigation/java/deploy/deployment.yaml](https://github.com/ml-for-good/automl/blob/main/Investigation/java/deploy/deployment.yaml)

部署命令：

```bash
kubectl apply -f automl-deployment.yaml
```

## License
