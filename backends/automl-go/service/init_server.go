/*
 * @author: 宋先生～
 * @brief:
 * @date:
 */
package service

import (
	"automl-go/components"
	"time"

	"automl-go/controller"

	"github.com/gin-gonic/gin"
)

/**
 ** @brief 	init system and start
 ** @param 	无
 ** @author 宋先生～
 ** @date 	2022.03.07
 **/
func Start() {
	gin.SetMode(GetConf().Server.Mode)
	router := gin.New()
	router.Use(components.Recovery(GetLog()))
	controller.Register(router)

	waitTimeout := time.Duration(GetConf().Server.ExitTimeoutSec) * time.Second   // wait duration
	readTimeout := time.Duration(GetConf().Server.ReadTimeoutSec) * time.Second   // read duration
	writeTimeout := time.Duration(GetConf().Server.WriteTimeoutSec) * time.Second // write duration
	go func() {
		address := "0.0.0.0:" + GetConf().Server.Port
		components.Run(address, waitTimeout, readTimeout, writeTimeout, router)
	}()

	components.WaitSignalGroupAllDone(waitTimeout)
}
