/**
 ** @brief 全局配置初始化
 ** @author 宋先生～
 ** @date 2022.03.07
**/

package httpd

import (
	"github.com/BurntSushi/toml"
	"github.com/cihub/seelog"
)

//RgeoConfig ...
type AutoMLConfig struct {
	Server server
}

type server struct {
	Disable         bool
	Mode            string
	Listen          string
	ReadTimeoutSec  int
	WriteTimeoutSec int
	ExitTimeoutSec  int
	DegradePort     int
}

var (
	// 请通过GetConf,GetLog获取全局变量
	gConf AutoMLConfig
	gLog  seelog.LoggerInterface
)

//GetConf ...
func GetConf() AutoMLConfig {
	return gConf
}

//SetConf ...
func SetConf(conf AutoMLConfig) {
	gConf = conf
}

//GetLog ...
func GetLog() seelog.LoggerInterface {
	return gLog
}

//SetLog ...
func SetLog(log seelog.LoggerInterface) {
	gLog = log
}

func InitConf() {
	//初始化日志
	log, err := seelog.LoggerFromConfigAsFile("config/log.xml")
	if err != nil {
		panic("解析seelog配置文件失败[config/log.xml]")
	}
	err = seelog.ReplaceLogger(log)
	if err != nil {
		panic("启动seelog失败")
	}
	SetLog(log)

	//读取cfg.toml的配置管理
	var conf AutoMLConfig
	_, decodeErr := toml.DecodeFile("./config/cfg.toml", &conf)
	if decodeErr != nil {
		log.Error(decodeErr.Error())
		log.Flush()
		panic("读取系统配置失败")
	}
	SetConf(conf)
	return
}

func InitServer() (err error) {
	//初始化服务配置
	InitConf()

	return
}
