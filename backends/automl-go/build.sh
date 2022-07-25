#!/bin/bash
###
 # @author: 宋先生～
 # @brief: 
 # @date: 
### 

workspace=$(cd $(dirname $0) && pwd -P)
cd ${workspace}
echo "workspace=${workspace}"

cwp=`pwd`

if [ ! -d "bin" ]; then
  mkdir bin
fi

if [ ! -d "logs" ]; then
  mkdir logs
fi

export PATH=$GOROOT/bin:$PATH
export GOSUMDB=off
export GO111MODULE=auto

if [ -d /usr/local/go1.16 ]; then
    export GOROOT=/usr/local/go1.16
else 
    export GOROOT=/usr/local/go
fi

if [ ! -d "$GOPATH" ]; then
    pushd $(dirname ${workspace})
    if [ ! -d "build" ]; then
        mkdir -p "build"
    fi
    cd build
    export GOPATH="$PWD"
    echo "GOPATH:$GOPATH"
    popd
fi
if [ ! -d "$GOPATH/src/" ]; then
    mkdir -p "$GOPATH/src/"
fi
ln -sf "${workspace}" "$GOPATH/src/automl-go"
cd "${workspace}"
export PATH=${GOROOT}/bin:$GOPATH/bin:${PATH}:$GOBIN

go clean -modcache
go mod vendor
rm -rf "automl-go"
go build -o "automl-go" "automl-go"
mv automl-go bin/

if [[ $? != 0 ]]; then
    echo -e "Build failed !"
    exit 1
fi
echo -n "Build success!"
