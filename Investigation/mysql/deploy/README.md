
# mysql deploy to k8s

>其实就是docker中安装mysql,  k8s进行管理docker，然后封装一层，提供集群存储和访问.

## 1、准备docker和k8s

[mac本地安装docker和k8s](https://www.freesion.com/article/1580745141/)

[docker中安装mysql:5.7之后](https://blog.csdn.net/qq_44697728/article/details/114550159?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.control&dist_request_id=1328740.51086.16170915053377201&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.control), 然后启动起来.


在docker中我们可以看到containers 证明mysql容器启动起来了.
![在这里插入图片描述](https://img-blog.csdnimg.cn/dacc2ee3851640c6afb337d91b28adf4.png)

## 2、k8s中创建mysql
首先得保证docker和k8s启动.
我们采用版本mysql  5.7
下面是具体的流程
### 2.1、创建namespace, 把mysql单独部署到这个空间
kubectl create namespace dev

### 2.2、创建持久卷PV, 来存储mysql数据文件
得先开启nfs服务.  很麻烦.
https://blog.csdn.net/nuptaxin/article/details/123958582

（1）定义一个容量大小为1GB的PV，挂载到/opt/nfs/jenkins 目录，需手动创建该目录

```
mkdir -p /opt/nfs/jenkins
```
（2）编写mysql-pv.yaml文件内容，要创建的pv对象名称：pv-1gi

```let message =
# 定义持久卷信息
apiVersion: v1
kind: PersistentVolume
metadata:
  # pv是没有namespace属性的，它是一种跨namespace的共享资源
  name: pv-1gi
spec:
  capacity:
    storage: 1Gi
  accessModes:
    - ReadWriteMany
  # 存储类，具有相同存储类名称的pv和pvc才能进行绑定
  storageClassName: nfs
  nfs:
    path: /opt/nfs/jenkins    # nfs的挂载地址
    server: 192.168.43.182    # nfs-server的ip地址
```

（3）创建该PV对象

```
kubectl create -f mysql-pv.yaml
```
（4）查看创建结果

```
kubectl describe pv pv-1gi
```

### 2.3、创建持久卷声明PVC
声明存储大小为1Gb的PVC资源，k8s会根据storageClassName存储类名称找到匹配的PV对象进行绑定。
（1）编写mysql-pvc.yaml文件内容，要创建的pvc对象名称是：mysql-pvc

```
# 定义mysql的持久卷声明信息
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: mysql-pvc
  namespace: dev
spec:
  accessModes:
    - ReadWriteMany
  resources:
    requests:
      storage: 1Gi
  # 存储类，具有相同存储类名称的pv和pvc才能进行绑定
  storageClassName: nfs
```

（2）创建该PVC对象

```
kubectl create -f mysql-pvc.yaml
```

（3）查看创建结果
可以看到mysql-pvc对象已经和pv-1gi对象绑定上了。

```
kubectl describe pvc mysql-pvc -n dev
```

### 2.4、创建Deployment 和 Service
（1）编辑mysql-svc.yaml文件内容
service使用NodePort类型，指定暴露的nodePort端口为31234，我们会在宿主机使用navicat客户端对mysql进行访问

```
# 定义mysql的Deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: mysql
  name: mysql
  namespace: dev
spec:
  selector:
    matchLabels:
      app: mysql
  template:
    metadata:
      labels:
        app: mysql
    spec:
      containers:
      - image: mysql:5.7     # docker容器imgame
        name: mysql
        env:
        - name: MYSQL_ROOT_PASSWORD
          value: "123456" 		# 密码
        ports:
        - containerPort: 3306
        volumeMounts:
        - name: mysqlvolume
          mountPath: /var/lib/mysql
      volumes:
      - name: mysqlvolume
        # 使用pvc
        persistentVolumeClaim:
          claimName: mysql-pvc
---
#定义mysql的Service
apiVersion: v1
kind: Service
metadata:
  labels:
    app: svc-mysql
  name: svc-mysql
  namespace: dev
spec:
  selector:
    app: mysql
  type: NodePort
  ports:
  - port: 3306
    protocol: TCP
    targetPort: 3306
    nodePort: 31234		# k8s 暴露出的mysql端口
```

（2）执行创建命令

```
kubectl create -f mysql-svc.yaml
```

（3）查看创建结果
可以看到mysql的pod已处于运行状态
```
kubectl get pod.svc -n dev
```
这样mysql已经running了.
![在这里插入图片描述](https://img-blog.csdnimg.cn/799ecef34a484d3298ce977f554e0a62.png)


3、测试

```
mysql -h 192.168.43.182 -P 31234  -uroot -p123456
```

192.168.43.182 是我的本机地址.   -P  31234就是 mysql-svc文件中的nodePort
ok。进来了.
![在这里插入图片描述](https://img-blog.csdnimg.cn/2b17afc3387c45f7af9981b81433079e.png)


4、总结命令
需要docker启动mysql
然后打开k8s
kubectl create namespace dev
kubectl create -f mysql-pv.yaml
kubectl create -f mysql-pvc.yaml
kubectl create -f mysql-svc.yaml
kubectl get pod,svc -n dev

相关文章:
一些踩坑
[https://blog.csdn.net/weixin_46415378/article/details/124482489](https://blog.csdn.net/weixin_46415378/article/details/124482489)
安装:
[https://cdn.modb.pro/db/399791](https://cdn.modb.pro/db/399791)

