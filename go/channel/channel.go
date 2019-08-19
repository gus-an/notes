package main

// import "fmt"
import "time"

// func main() {
// 	ch := make(chan int)

// 	go func() {
// 		ch <- 123 
// 	}()

// 	var i int
// 	i = <- ch
// 	println(i)
// }

// func main() {
// 	done := make(chan bool)

// 	go func() {
// 		for i := 0; i < 10; i++ {
// 			fmt.Println(i)
// 		}
// 		done <- true
// 	}()

// 	<- done
// }

// func main() {
// 	ch := make(chan int, 2)

// 	ch <- 1
// 	ch <- 2

// 	close(ch)

// 	println(<-ch)

// 	if recv, success := <-ch; !success {
// 		println("더이상 데이터 없음")
// 	} else {
// 		println(recv)
// 	}
// }

// func main() {
// 	ch := make(chan int, 2)

// 	ch <- 1
// 	ch <- 2

// 	close(ch)

// 	for i := range ch {
// 		println(i)
// 	}
// }

func main() {
	done1 := make(chan bool)
	done2 := make(chan bool)

	go run1(done1)
	go run2(done2)

EXIT:
	for {
		select {
		case <- done1:
			println("run1 완료")
		case <- done2:
			println("run2 완료")
			break EXIT
		}
	}	
}

func run1(done chan bool){
	time.Sleep(time.Second)
	done <- true
}

func run2(done chan bool){
	time.Sleep(time.Second * 2 )
	done <- true
}