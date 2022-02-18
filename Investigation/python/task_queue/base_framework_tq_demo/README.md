## 基于flask-restful和celery(未实现)的机器学习服务框架(demo)

### run
0. 安装docker
1. `docker build . -t app_service`
2. `docker run -it -p 8030:8030 app_service`, 后台启动+ `-d`

### 测试
`curl -X POST -d '{"name":"h2222"}' http://127.0.0.1:8030/tq`


### 介绍
一个restful风格的机器学习服务框架, 可以轻松的开发组件并测试, 并支持多种请求形式(handler)<br/>
优势1. 灵活开发, 用户只要实现component的子类即可用于服务<br/>
优势2. 配置化, 灵活组合需要的component<br/>
优势3. 支持长时任务队列(基于Celery的Pipeline, 未实现)<br/>
```
加载顺序:
1. handler.initialize (app.py) 读取配置文件config/xx.json
2. pipeline.load()(base_handler.py) 读取配置文件中component并进行实例化, 加载当前component的配置信息
3. 某个Compoment的的子类(test_comp/), 加载配置信息


服务顺序:
1. query 
2. handler.post/get
3. handler.process
4. pipeline.process
5. [comp1.process, comp2.process, comp3.process]
6. result
```