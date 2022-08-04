## 环境
1. `jdk: 17`
2. `docker`
3. `minikube`

## 命令行build
1. `在deploy目录下运行docker build . -t deploy:0.0.2 --build-arg JAR_FILE="target/deploy-0.0.2.jar"`

## maven插件build
1. `设置环境变量DOCKER_HOST=tcp://{docker_host}:2375, (tls需要额外设置变量)`
2. `在deploy目录下执行mvn dockerfile:build`

## run
1. `minikube start`
2. `eval $(minikube docker-env)`
3. `kubectl create -f deployment.yaml`

```bash

➜  minikube service deploy-demo

|-----------|-------------|-------------|---------------------------|
| NAMESPACE |    NAME     | TARGET PORT |            URL            |
|-----------|-------------|-------------|---------------------------|
| default   | deploy-demo |        8080 | http://192.168.49.2:32278 |
|-----------|-------------|-------------|---------------------------|
```

```bash
➜  curl -v http://192.168.49.2:32278/demo/test

* About to connect() to 192.168.49.2 port 32278 (#0)
*   Trying 192.168.49.2...
* Connected to 192.168.49.2 (192.168.49.2) port 32278 (#0)
> GET /demo/test HTTP/1.1
> User-Agent: curl/7.29.0
> Host: 192.168.49.2:32278
> Accept: */*
> 
< HTTP/1.1 200 
< Content-Type: text/plain;charset=UTF-8
< Content-Length: 4
< Date: Fri, 29 Jul 2022 17:00:50 GMT
< 
* Connection #0 to host 192.168.49.2 left intact
true%  
```