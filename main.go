// +build linux,cgo
package main

import "C"
import "fmt"

func main() {
	fmt.Printf("***** THIS IS MAIN ****")
}

//export SendRemind
func SendRemind(str string) *C.char {

	s := fmt.Sprintf("**** SendRemind: Hello %s\n", str)
	fmt.Printf(s)
	return C.CString(s)
}

//export Add
func Add(a, b int) int {
	fmt.Printf("**** Parameters : a=[%d], b=[%d]\n", a,b)
	fmt.Printf("**** Add:  %d\n", a+b)

	return a + b
}
