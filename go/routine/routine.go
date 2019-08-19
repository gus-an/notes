 package main

import (
	"fmt"
	"time"
	"sync"
)

// func say(s string) {
// 	for i := 0; i < 3; i++ {
// 		fmt.Println(s, "***", i)
// 	}
// }

// func main() {
// 	say("Sync")

// 	go say("Async1")
// 	go say("Async2") 
// 	go say("Async3")

// 	time.Sleep(time.Second * 1)
// }

func main() {
	var wait sync.WaitGroup
	wait.Add(2) // 몇 개의 routine을 기다릴지 지정

	go func() {
		defer wait.Done()
		time.Sleep(time.Second * 1)
		fmt.Println("Hello")
	}()

	go func(msg string) {
		defer wait.Done()
		fmt.Println(msg)
	}("Hi")

	wait.Wait()
}