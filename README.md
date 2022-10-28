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

开始之前,请确保以下组件安装在你的机器上:

- Docker: (参考:https://docs.docker.com/desktop/install/mac-install/）
- Minikube:  (参考:https://minikube.sigs.k8s.io/docs/start/)
- Helm:(参考:https://helm.sh/zh/docs/)

**Mac OS:**

Minikube在macOS上首选驱动为Docker。

- 启动Docker
- 使用 Docker驱动启动集群：`minikube start --driver=docker`
- 配置Docker为默认驱动程序：`minikube config set driver docker`
- 执行`kubectl get node` 验证启动是否成功。

**Linux:** Todo

**Windows:**

Minikube在Windows上首选驱动为Hyper-V+Docker。我们使用Docker来作为驱动程序。

- 启动Docker
- 使用 Docker 驱动启动集群：`minikube start --driver=docker`
- 配置 Docker 为默认驱动程序：`minikube config set driver docker`
- 执行`kubectl get node` 验证启动是否成功


**加载本地镜像到 minikube:**
构建镜像:
```bash
docker build -t automl/automl:v1beta1 java/automl
```

加载本地镜像：
```bash
minikube image load automl/automl:v1beta1 # minikube image load <image>, your local image
```

### Start Deploy

配置**automl**仓库: 

```bash
helm repo add automl https://ml-for-good.github.io/automl/
```

搜索automl仓库下的chart:

```bash
helm search repo automl
```

安装automl的helm包：

```bash
helm install automl automl/deploy
```

查看pod,svc,deployment信息:

```bash
kubectl get pod,svc,deployment,pv,pvc -n mysql
```

### 测试Mysql连接

获取 minikube的 `IP` 和service的`NodePort`

```bash
minikube service mysql -n mysql --url
```

使用本地Navicat客户端连接数据库,连接信息:

``Host:IP``

``port:NodePort``

``用户名:root``

``密码:root``

进入之后, 可以看到库automl和automl-test和相关表已经创建了.

### Test OpenAPI mock server

Run service tunnel

```bash
minikube service openapi-mock
```

Try in your browser

Open in your browser (ensure there is no proxy set)

http://127.0.0.1:TUNNEL_PORT/v1beta1/namespaces/1/datasets

### Test AUTOML java web demo server

Load local image to minikube

```bash
minikube image load automl/automl:v1 # minikube image load <image>, your local image
```
Run service tunnel

```bash
minikube service automl-web
```

Try in your browser

Open in your browser (ensure there is no proxy set)

http://127.0.0.1:TUNNEL_PORT/swagger-ui/index.html

Get pod, deployment status, name
```bash
kubectl get pod,deployment
```

Get logs
```bash
kubectl logs <resource name>
```

### Stop automl-web pod & deployment

```bash
kubectl delete deploy automl-web
```

### switch java application link mysql prod.

> 默认java/automl/目录下的Dockerfile中的 -Dspring.profiles.active=dev 环境是dev环境, 采用automl库

> 在本地自己测试部署的时候, 可以修改这个值为test这样, automl-web 服务采用automl-test库.

#### test link

> 部署完automl-web之后, 本地执行以下命令.

```
curl -X POST "http://127.0.0.1:TUNNEL_PORT/v1beta1/test/insert" -H "accept: /" -H "Content-Type: application/json" -d "{ "id": 160676, "name": "sss"}"
```

我们可以看到已经有数据了. (我当时是以test环境启动的)
![在这里插入图片描述](https://img-blog.csdnimg.cn/e628364a4f1d4d89b7f25b5096a337bd.png)

Todo

## License
