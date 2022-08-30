

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

- Docker
- Minikube

如果没有，参考如下安装教程:

**Mac OS:**

Minikube在macOS上首选驱动为Docker。

- 启动Docker
- 下载Minikube: `brew install minikube`
- 使用 docker 驱动启动集群：`minikube start --driver=docker`
- 配置docker 为默认驱动程序：`minikube config set driver docker`
- 执行`kubectl get node` 验证启动是否成功。

**Linux:** Todo

**Windows:**

Minikube在Windows上首选驱动为Hyper-V+Docker。我们使用Docker来作为驱动程序。

- 启动Docker
- 下载`minikube.exe`文件，然后将`minikube.exe`添加到环境变量的`PATH`中。
- 使用 docker 驱动启动集群：`minikube start --driver=docker`
- 配置docker 为默认驱动程序：`minikube config set driver docker`
- 执行`kubectl get node` 验证启动是否成功

### Start Deploy

开始部署前,确保启动minikube和获取最新部署文件!!!

在``automl``目录下执行命令:

```bash
kubectl apply -f deploy
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


### Test OpenAPI mock server

Run service tunnel

```bash
minikube service openapi-mock
```

Try in your browser

Open in your browser (ensure there is no proxy set)

http://127.0.0.1:TUNNEL_PORT/v1beta1/namespaces/1/datasets

## License

Todo
