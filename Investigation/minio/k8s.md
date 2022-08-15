1. 包含以下`minio-dev.yaml`Kubernetes 资源：

   ```
   # Deploys a new Namespace for the MinIO Pod
   apiVersion: v1
   kind: Namespace
   metadata:
     name: minio-dev # Change this value if you want a different namespace name
     labels:
       name: minio-dev # Change this value to match metadata.name
   ---
   # Deploys a new MinIO Pod into the metadata.namespace Kubernetes namespace
   #
   # The `spec.containers[0].args` contains the command run on the pod
   # The `/data` directory corresponds to the `spec.containers[0].volumeMounts[0].mountPath`
   # That mount path corresponds to a Kubernetes HostPath which binds `/data` to a local drive or volume on the worker node where the pod runs
   #
   apiVersion: v1
   kind: Pod
   metadata:
     labels:
       app: minio
     name: minio
     namespace: minio-dev # Change this value to match the namespace metadata.name
   spec:
     containers:
     - name: minio
       image: quay.io/minio/minio:latest
       command:
       - /bin/bash
       - -c
       args:
       - minio server /data --console-address :9090
       volumeMounts:
       - mountPath: /data
         name: localvolume # Corresponds to the `spec.volumes` Persistent Volume
     nodeSelector:
       kubernetes.io/hostname: kubealpha.local # Specify a node label associated to the Worker Node on which you want to deploy the pod.
     volumes:
     - name: localvolume
       hostPath: # MinIO generally recommends using locally-attached volumes
         path: /mnt/disk1/data # Specify a path to a local drive or volume on the Kubernetes worker node
         type: DirectoryOrCreate # The path to the last directory must exist
   ```

   该对象部署了两个资源：

   - 一个新的命名空间`minio-dev`，和
   - 使用 Worker 节点上的驱动器或卷来提供数据的 MinIO pod

   MinIO 资源定义使用 Kubernetes[节点选择器和标签](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#built-in-node-labels)将 pod 限制为具有匹配主机名标签的节点。用于查看分配给集群中每个节点的所有标签。`kubectl get nodes --show-labels`

   MinIO Pod 使用[hostPath](https://kubernetes.io/docs/concepts/storage/volumes/#hostpath)卷来存储数据。此路径*必须*对应于 Kubernetes 工作程序节点上的本地驱动器或文件夹。

   熟悉 Kubernetes 调度和卷配置的用户可以修改`spec.nodeSelector`、`volumeMounts.name`和`volumes`字段以满足更具体的要求。

2. **应用 MinIO 对象定义**

   以下命令应用`minio-dev.yaml`配置并将对象部署到 Kubernetes：

   ```
   kubectl apply -f minio-dev.yaml
   ```


   命令输出应类似于以下内容：

   ```
   namespace/minio-dev created
   pod/minio created
   ```

   您可以通过运行来验证 pod 的状态：`kubectl get pods`

   ```
   kubectl get pods -n minio-dev
   ```


   输出应类似于以下内容：

   ```
   NAME    READY   STATUS    RESTARTS   AGE
   minio   1/1     Running   0          77s
   ```

   您还可以使用以下命令检索有关 pod 状态的详细信息：

   ```
   kubectl describe pod/minio -n minio-dev

   kubectl logs pod/minio -n minio-dev
   ```


3. **临时访问 MinIO S3 API 和控制台**

   使用命令将流量从 MinIO pod 临时转发到本地机器：`kubectl port-forward`

   ```
   kubectl port-forward pod/minio 9000 9090
   ```


   该命令将 pod 端口转发到本地机器上的匹配端口，同时在 shell 中处于活动状态`9000`。`9090`该命令仅在 shell 会话中处于活动状态时起作用。终止会话会关闭本地计算机上的端口。`kubectl port-forward`

   笔记

   此过程的以下步骤假定一个活动命令。`kubectl port-forward`

   要配置对 pod 的长期访问，请在 Kubernetes 中配置[Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/)或类似的网络控制组件，以路由进出 pod 的流量。配置 Ingress 超出了本文档的范围。

4. **将您的浏览器连接到 MinIO 服务器**

   通过在本地计算机上打开浏览器并导航到.来访问[MinIO 控制台](https://docs.min.io/minio/baremetal/console/minio-console.html#minio-console)`http://127.0.0.1:9090`。

   使用凭据登录到控制台。这些是默认的[root 用户](https://docs.min.io/minio/baremetal/security/minio-identity-management/user-management.html#minio-users-root)凭据。`minioadmin | minioadmin`