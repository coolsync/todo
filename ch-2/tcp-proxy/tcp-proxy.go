package main

import (
	"io"
	"log"
	"net"
)

func main() {
	liser, err := net.Listen("tcp", ":80")
	if err != nil {
		log.Fatal(err)
	}
	log.Println("listen port ok!")
	for {
		conn, err := liser.Accept()
		if err != nil {
			log.Fatal(err)
		}
		go handler(conn)
	}
}

func handler(src net.Conn) {
	dst, err := net.Dial("tcp", "www.baidu.com:80")
	if err != nil {
		log.Println("net dial err")
		return
	}
	defer dst.Close()
	
	go func ()  {
		if _, err := io.Copy(dst, src); err != nil {
			log.Fatal(err)
		}
	}()

	if _, err := io.Copy(src, dst); err != nil {
		log.Fatal(err)
	}
}