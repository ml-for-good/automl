FROM golang
copy . /$GOPATH/src/AutoML/
workdir /$GOPATH/src/AutoML/
#设置环境变量
RUN go env -w GO111MODULE=on
RUN go env -w GOPROXY=https://goproxy.cn,direct
EXPOSE 9000:9000