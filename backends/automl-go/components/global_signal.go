/*
 * 解决程序有多个信号量问题,且需要等待全部执行完成
 */
package components

import (
	"log"
	"os"
	"os/signal"
	"sync"
	"syscall"
	"time"
)

var (
	wg sync.WaitGroup
)

/*
 * 参数：
 *   isAutoDone: 主要是用于确认只要返回信号量就认为已完成
 */
func RegisterInterruptSignal(name string, isAutoDone bool) *GlobalSignal {
	signal := GlobalSignal{
		name:       name,
		interrupt:  make(chan os.Signal, 1),
		isDone:     false,
		isAutoDone: isAutoDone,
	}
	signal.Init()

	log.Printf("RegisterInterruptSignal[name:%s][isAutoDone:%t]", name, isAutoDone)
	wg.Add(1)
	return &signal
}

/*
 * 如果使用此方法，默认就主程序也监听信号量，并等待
 */
func WaitSignalGroupAllDone(timeout time.Duration) {
	log.Printf("WaitSignalGroupAllDone begin")
	globalSignal := RegisterInterruptSignal("main process", true) // 注册主程序监控信号量
	globalSignal.Wait()                                           // 等待主程序信号量的完成

	c := make(chan bool)
	go func() {
		log.Printf("WaitSignalGroupAllDone wait go begin")
		wg.Wait() //等待所有信号量的完成
		c <- true
		log.Printf("WaitSignalGroupAllDone wait go end")
	}()
	select {
	case <-c:
		log.Printf("WaitSignalGroupAllDone select wait success end")
	case <-time.After(timeout):
		log.Printf("WaitSignalGroupAllDone select timeout end")
	}

}

type GlobalSignal struct {
	name       string
	interrupt  chan os.Signal
	isDone     bool
	isAutoDone bool // 是否需要自动完成。对应已有连接需要等待完成请求后，才全部结束
	lock       sync.Mutex
}

func (this GlobalSignal) Init() {
	signal.Notify(this.interrupt, syscall.SIGINT, syscall.SIGTERM, syscall.SIGQUIT)
}

func (this GlobalSignal) IsCatched(waitTimeout int) (catched bool, sig os.Signal) {

	timeout := time.Duration(waitTimeout) * time.Second
	catched = false

	select {
	case sig = <-this.interrupt:
		catched = true
	case <-time.After(timeout):
		catched = false
	}

	if catched {
		this.finish()
	}
	return catched, sig
}

func (this GlobalSignal) Wait() (sginal os.Signal) {
	signal := <-this.interrupt
	this.finish()
	return signal
}

func (this GlobalSignal) Done() {
	log.Printf("[%s][%t] Done wg begin", this.name, this.isAutoDone)
	if !this.isAutoDone {
		log.Printf("[%s] Done wg done", this.name)
		wg.Done()
	}
}

// 处理信号量是否已完全结束
func (this GlobalSignal) finish() {
	log.Printf("[%s] receive signal", this.name)
	this.lock.Lock()
	defer this.lock.Unlock()

	if !this.isDone {
		this.isDone = true

		if this.isAutoDone {
			log.Printf("[%s] finish wg done", this.name)
			wg.Done()
		}
	}
}
