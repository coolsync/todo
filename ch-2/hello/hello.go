package main

import (
	"log"
	"net"
)

func main() {
	dst, err := net.Dial("tcp", "www.baidu.com:80")
	if err != nil {
		log.Fatalln("net dial err")
	}
	defer dst.Close()	
}
