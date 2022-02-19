package main

import (
	"automl/v1/worker"
)

func main() {
	taskWorker := worker.NewAsyncTaskWorker(0)
	taskWorker.Launch()
}
