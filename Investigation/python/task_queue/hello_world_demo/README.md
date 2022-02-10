### hello world 服务demo在docker容器中的运行步骤
1. 下载docker destop, 可以使用`docker --help`检测是否已经安装成功
2. 在项目目录下运行`docker build -t hello-test .`构建镜像
3. 在项目目录下运行`docker run -p 80:8030 -d hello-test`运行容器, 其中80为本地端口, 8030为容器端口
4. 在浏览器中输入`localhost:80/hello`访问服务, 如果看到hello world则说明创建成功

### hello world 服务demo在minikube中的部署的运行步骤
1. 下载安装`minikube`
2. 运行`kubectl apply -f deployment.yaml`, 看到服务出现`create`或者 `unchange`说明运行成功
3. 运行 `kubectl get pods` 查看Pod(容器), 运行 `kubectl get services` 查看服务, 其中`kubernetes`为minikube启动的服务
4. 运行 `minikube service hello-test-np-service` 会自动跳转的浏览器页面, 如果返回结果说明正常

ps: [如何启用本地镜像](https://medium.com/swlh/how-to-run-locally-built-docker-images-in-kubernetes-b28fbc32cc1d)
在build本地镜像后, 输入`eval $(minikube -p minikube docker-env)`, 后在进行apply, 查看`kubectl get pods`观察pods状态, 如果为`running`说明运行成功, 如果为`ErrImageNeverPull`为失败.