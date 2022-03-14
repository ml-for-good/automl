/**
 ** @brief 初始化系统框架,启动服务
 ** @author 宋先生～
 ** @date 2022.03.07
**/

package httpd

import (
	"automl-go/components"
	"time"

	srouter "automl-go/controller"

	"github.com/gin-gonic/gin"
)

/**
 ** @brief 	初始化系统框架,启动服务
 ** @param 	无
 ** @author 宋先生～
 ** @return 成功返回nil,失败返回对应的error
 ** @date 	2022.03.07
 **/
func Start() {
	// 开始初始化框架
	gin.SetMode(GetConf().Server.Mode)
	// gin.New() 取消自定义的loggger() recovery()
	router := gin.New()
	// 配置内部程序使用自定义的panic捕获, 自动记录日志等
	router.Use(components.Recovery(GetLog()))
	// 注册路由
	srouter.Register(router)

	// waitTimeout: 等待多长时间退出
	waitTimeout := time.Duration(GetConf().Server.ExitTimeoutSec) * time.Second
	// readTimeout: http server读超时
	readTimeout := time.Duration(GetConf().Server.ReadTimeoutSec) * time.Second
	// writeTimeout: http server 写超时
	writeTimeout := time.Duration(GetConf().Server.WriteTimeoutSec) * time.Second
	go func() {
		address := GetConf().Server.Listen
		components.GracefulRun(address, waitTimeout, readTimeout, writeTimeout, router)
	}()

	components.WaitSignalGroupAllDone(waitTimeout)
}
