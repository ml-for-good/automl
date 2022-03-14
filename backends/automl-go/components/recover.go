/*
 * 处理gin框架的内部异常
 * 定义了NewGo,集合了recover和go，统一处理异常
 */
package components

import (
	"bytes"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"reflect"
	"runtime"

	"github.com/cihub/seelog"

	"github.com/gin-gonic/gin"
)

var (
	dunno     = []byte("???")
	centerDot = []byte("·")
	dot       = []byte(".")
	slash     = []byte("/")
)

// Recovery returns a middleware that recovers from any panics and writes a 500 if there was one.
func Recovery(log seelog.LoggerInterface) gin.HandlerFunc {
	return RecoveryWithWriter(log)
}

func RecoveryWithWriter(log seelog.LoggerInterface) gin.HandlerFunc {
	return func(c *gin.Context) {
		defer func() {
			if err := recover(); err != nil {
				if log != nil {
					stack := stack(3)
					log.Errorf("Panic recovery -> %s\n%s\n", err, stack)
				}
				http.Error(c.Writer, "服务器内部错误", http.StatusInternalServerError)
				c.Abort()

			}
		}()
		c.Next()
	}
}

/*
 * goroute默认注册全局信号量,
 * 防止主进程退出后，goroute还未完成
 *
 */
func Go(params *map[string]interface{}, callback func(*map[string]interface{})) {
	f := func(params *map[string]interface{}) {
		funName := runtime.FuncForPC(reflect.ValueOf(callback).Pointer()).Name()
		globalSignal := RegisterInterruptSignal(funName, true)
		defer func() {
			globalSignal.Done()
			if err := recover(); err != nil {
				stack := stack(3)
				log.Printf("Panic recovery -> %s\n%s\n", err, stack)
				// TODO
				// 发送堆栈信息邮件至Admin
			}
		}()
		callback(params)
	}
	go f(params)
}

// stack returns a nicely formated stack frame, skipping skip frames
func stack(skip int) []byte {
	buf := new(bytes.Buffer) // the returned data
	// As we loop, we open files and read them. These variables record the currently
	// loaded file.
	var lines [][]byte
	var lastFile string
	for i := skip; ; i++ { // Skip the expected number of frames
		pc, file, line, ok := runtime.Caller(i)
		if !ok {
			break
		}
		// Print this much at least.  If we can't find the source, it won't show.
		fmt.Fprintf(buf, "%s:%d (0x%x)\n", file, line, pc)
		if file != lastFile {
			data, err := ioutil.ReadFile(file)
			if err != nil {
				continue
			}
			lines = bytes.Split(data, []byte{'\n'})
			lastFile = file
		}
		fmt.Fprintf(buf, "\t%s: %s\n", function(pc), source(lines, line))
	}
	return buf.Bytes()
}

// source returns a space-trimmed slice of the n'th line.
func source(lines [][]byte, n int) []byte {
	n-- // in stack trace, lines are 1-indexed but our array is 0-indexed
	if n < 0 || n >= len(lines) {
		return dunno
	}
	return bytes.TrimSpace(lines[n])
}

// function returns, if possible, the name of the function containing the PC.
func function(pc uintptr) []byte {
	fn := runtime.FuncForPC(pc)
	if fn == nil {
		return dunno
	}
	name := []byte(fn.Name())
	// The name includes the path name to the package, which is unnecessary
	// since the file name is already included.  Plus, it has center dots.
	// That is, we see
	//	runtime/debug.*T·ptrmethod
	// and want
	//	*T.ptrmethod
	// Also the package path might contains dot (e.g. code.google.com/...),
	// so first eliminate the path prefix
	if lastslash := bytes.LastIndex(name, slash); lastslash >= 0 {
		name = name[lastslash+1:]
	}
	if period := bytes.Index(name, dot); period >= 0 {
		name = name[period+1:]
	}
	name = bytes.Replace(name, centerDot, dot, -1)
	return name
}
