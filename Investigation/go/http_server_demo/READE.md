# 通过 minikube start
# 进入 minikube dashboard
# 执行 kubectl create -f deployment.yml
# 执行 kubectl expose deployment hello-node --type=LoadBalancer --port=9000
# 执行 minikube service hello-node



# go task queue demo 注意需要本地启动 redis server
# 1. 运行 main.go
# 2. 运行 sendtask.go
# 可查看出触发的 demo 样例