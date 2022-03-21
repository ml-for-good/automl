/*
 * @author: 宋先生～
 * @brief: init config and log
 * @date:
 */
package service

import (
	"github.com/cihub/seelog"
	"gopkg.in/ini.v1"
)

type AutoMLConfig struct {
	Server server
}

type server struct {
	Mode            string `ini:"mode"`
	Port            string `ini:"port"`
	ReadTimeoutSec  int    `ini:"readTimeoutSec"`
	WriteTimeoutSec int    `ini:"writeTimeoutSec"`
	ExitTimeoutSec  int    `ini:"exitTimeoutSec"`
}

// Get log and config by GetConf,GetLog func
var (
	globalConf AutoMLConfig
	globalLog  seelog.LoggerInterface
)

func GetConf() AutoMLConfig {
	return globalConf
}

func SetConf(conf AutoMLConfig) {
	globalConf = conf
}

func GetLog() seelog.LoggerInterface {
	return globalLog
}

func SetLog(log seelog.LoggerInterface) {
	globalLog = log
}

func InitConf() {
	log, err := seelog.LoggerFromConfigAsFile("../conf/log_conf.xml")
	if err != nil {
		panic("parse log file error")
	}
	err = seelog.ReplaceLogger(log)
	if err != nil {
		panic("launch logger error")
	}
	SetLog(log)

	var conf AutoMLConfig
	conf.Server = server{}
	err = ini.MapTo(&conf.Server, "../conf/src_conf.ini")
	if err != nil {
		log.Error(err)
		log.Flush()
		panic("parse src_conf.ini file error")
	}
	SetConf(conf)
	return
}

func Init() {
	InitConf()
	// TODO
	return
}
