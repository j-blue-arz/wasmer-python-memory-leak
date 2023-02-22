package main

import "fmt"

//go:export hello
func hello() {
	fmt.Println("Hello World!")
}

func main() {}
