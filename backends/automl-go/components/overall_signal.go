/*
 * resolve mutil signal, and all signal complete
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

func WaitSignalGroupAllDone(timeout time.Duration) {
	log.Printf("WaitSignalGroupAllDone begin")
	overallSignal := RegisterInterruptSignal("main process", true) // regist main signal
	overallSignal.Wait()                                           // wait main signal complete

	c := make(chan bool)
	go func() {
		log.Printf("WaitSignalGroupAllDone wait go begin")
		wg.Wait() //wait all sighal
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

func RegisterInterruptSignal(name string, isAutoDone bool) *OverallSignal {
	signal := OverallSignal{
		name:       name,
		interrupt:  make(chan os.Signal, 1),
		isDone:     false,
		isAutoDone: isAutoDone,
	}
	signal.Init()

	wg.Add(1)
	return &signal
}

type OverallSignal struct {
	name       string
	interrupt  chan os.Signal
	isDone     bool
	isAutoDone bool
	lock       sync.Mutex
}

func (os OverallSignal) Init() {
	signal.Notify(os.interrupt, syscall.SIGINT, syscall.SIGTERM, syscall.SIGQUIT)
}

func (os OverallSignal) IsCatched(waitTimeout int) (catched bool, sig os.Signal) {

	timeout := time.Duration(waitTimeout) * time.Second
	catched = false

	select {
	case sig = <-os.interrupt:
		catched = true
	case <-time.After(timeout):
		catched = false
	}

	if catched {
		os.finish()
	}
	return catched, sig
}

func (os OverallSignal) Wait() (sginal os.Signal) {
	signal := <-os.interrupt
	os.finish()
	return signal
}

func (os OverallSignal) Done() {
	if !os.isAutoDone {
		wg.Done()
	}
}

func (os OverallSignal) finish() {
	os.lock.Lock()
	defer os.lock.Unlock()

	if !os.isDone {
		os.isDone = true

		if os.isAutoDone {
			wg.Done()
		}
	}
}
