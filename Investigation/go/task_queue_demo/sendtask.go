package main

import (
	"automl/v1/worker"
	"context"
)

func main() {
	worker.SendHelloWorldTask(context.Background())
}
