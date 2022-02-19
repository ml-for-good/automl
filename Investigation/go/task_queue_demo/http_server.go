package main

import (
	"context"
	"net/http"

	"automl/v1/worker"

	"github.com/gin-gonic/gin"
)

func main() {
	// 1.创建路由
	r := gin.Default()
	// 2.绑定路由规则，执行的函数
	r.GET("/", func(c *gin.Context) {
		worker.SendHelloWorldTask(context.Background())
		c.String(http.StatusOK, "hello World!")
	})
	// 3.监听端口，默认在8080
	// Run("里面不指定端口号默认为9000")
	r.Run(":9000")
}
