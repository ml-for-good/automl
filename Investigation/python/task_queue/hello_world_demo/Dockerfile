# 加载基础镜像(docker hub中可以找到)
FROM python:3.7-slim-buster
# 指定之后docker命令的工作路径
WORKDIR /hello_test
# 将本地目录的下的文件拷贝到docker镜像的WORKDIR中
COPY . .
# 创建镜像的命令
RUN pip3 install -r requirments.txt
# 创建镜像完成后, 指定容器运行的命令
CMD ["python3", "app.py"]