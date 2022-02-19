# 1. 启动minikube， 命令: minikube start
# 2. 启动 Redis 服务， 命令: kubectl create -f deploy/redis.yaml
# 3. 启动 worker 服务， 命令: kubectl create -f deploy/worker.yaml
# 4. 启动 web 服务, 命令: kubectl create -f deploy/web.yaml


# 第一种: 运行 访问web服务, 命令: minikube service list, 找到go-web url进行访问。
# 第二种: 进入到go-worker pod 内部，运行 go run senbtask.go, 然后查看go-worker pod的日志即可.