下载安装 minikube
运行 minikube start --kubernetes-version=v1.23.8 --image-mirror-country=cn（如果在国内）
运行 kubectl apply -f test.yaml
运行 kubectl get pods 查看Pod
运行 kubectl get services 查看服务
运行 minikube service test-demo-np-service 会自动跳转的浏览器页面, 如果返回结果说明正常


启用本地镜像
-运行 minikube -p minikube docker-env（windows环境）
-运行 docker build -t test-demo .
-运行 kubectl get pods 观察pods状态, 如果为`running`说明运行成功, 如果为`ErrImageNeverPull`为失败. 

感谢前一位老哥。