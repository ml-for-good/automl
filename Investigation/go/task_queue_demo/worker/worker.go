package worker

import (
	"github.com/RichardKnop/machinery/v1"
	mchConf "github.com/RichardKnop/machinery/v1/config"
	"github.com/RichardKnop/machinery/v1/log"
	"github.com/RichardKnop/machinery/v1/tasks"
)

var (
	AsyncTaskCenter *machinery.Server
)

func init() {
	tc, err := NewTaskCenter()
	if err != nil {
		panic(err)
	}
	AsyncTaskCenter = tc
}

func NewTaskCenter() (*machinery.Server, error) {
	cnf := &mchConf.Config{
		Broker:        "redis://localhost:6379",
		DefaultQueue:  "ServerTasksQueue",
		ResultBackend: "redis://localhost:6379",
	}
	// Create server instance
	server, err := machinery.NewServer(cnf)
	if err != nil {
		return nil, err
	}
	initAsyncTaskMap()
	return server, server.RegisterTasks(asyncTaskMap)
}

func NewAsyncTaskWorker(concurrency int) *machinery.Worker {
	consumerTag := "TestWorker"
	// The second argument is a consumer tag
	// Ideally, each worker should have a unique tag (worker1, worker2 etc)
	worker := AsyncTaskCenter.NewWorker(consumerTag, concurrency)
	// Here we inject some custom code for error handling,
	// start and end of task hooks, useful for metrics for example.
	errorhandler := func(err error) {
		log.ERROR.Println("I am an error handler:", err)
	}
	pretaskhandler := func(signature *tasks.Signature) {
		log.INFO.Println("I am a start of task handler for:", signature.Name)
	}
	posttaskhandler := func(signature *tasks.Signature) {
		log.INFO.Println("I am an end of task handler for:", signature.Name)
	}
	worker.SetPostTaskHandler(posttaskhandler)
	worker.SetErrorHandler(errorhandler)
	worker.SetPreTaskHandler(pretaskhandler)
	return worker
}
