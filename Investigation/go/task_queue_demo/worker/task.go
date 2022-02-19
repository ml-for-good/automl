package worker

import (
	"context"
	"fmt"

	"github.com/RichardKnop/machinery/v1/tasks"
)

var (
	asyncTaskMap map[string]interface{}
)

// 方法名
const (
	HelloWorldTaskName          = "HelloWorldTask"
	DeleteAppShareImageTaskName = "DeleteAppShareImageTask"
)

// HelloWorld 测试异步任务
func HelloWorld() error {
	fmt.Println("Hello World!")
	return nil
}

// SendHelloWorldTask 调用点调用此异步任务函数
func SendHelloWorldTask(ctx context.Context) {
	args := make([]tasks.Arg, 0)
	task, _ := tasks.NewSignature(HelloWorldTaskName, args)
	task.RetryCount = 5
	AsyncTaskCenter.SendTaskWithContext(ctx, task)
}

func initAsyncTaskMap() {
	asyncTaskMap = make(map[string]interface{})
	asyncTaskMap[HelloWorldTaskName] = HelloWorld
}
