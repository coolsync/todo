package main

import (
	"bufio"
	"log"
	"net"
)

// func echo(conn net.Conn) {
// 	defer conn.Close()

// 	buf := make([]byte, 512)
// 	for {

// 		n, err := conn.Read(buf[:])
// 		if n == 0 {
// 			return
// 		}
// 		if err != nil {
// 			log.Fatalln("unable to read data")
// 		}
// 		log.Printf("received %d bytes: %s\n", n, string(buf[:n]))

// 		if _, err := conn.Write(buf[:n]); err != nil {
// 			log.Fatal(err)
// 		}
// 	}
// }

func echo(conn net.Conn) {
	defer conn.Close()

	reader := bufio.NewReader(conn)
	writer := bufio.NewWriter(conn)

	for {
		s, err := reader.ReadString('\n')
		if err != nil {
			log.Fatal(err)
		}

		log.Printf("received %d bytes: %s\n", len(s), s)
		if _, err := writer.WriteString(s); err != nil {
			log.Fatal(err)
		}
		
		writer.Flush()
	}
}
func main() {
	liser, err := net.Listen("tcp", ":20080")
	if err != nil {
		log.Fatal(err)
	}
	log.Println("listen port ok!")
	for {
		conn, err := liser.Accept()
		if err != nil {
			log.Fatal(err)
		}
		go echo(conn)
	}
}
