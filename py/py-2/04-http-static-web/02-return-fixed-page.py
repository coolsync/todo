import socket

if __name__ == '__main__':
    ser_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    ser_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    ser_socket.bind(("", 8081))

    ser_socket.listen(128)

    while True:
        # read recv data
        new_socket, ip_port = ser_socket.accept()

        recv_data = new_socket.recv(4096) 

        recv_con = recv_data.decode('utf-8')
        
        print(recv_con)

        # send data to client
        with open('static/index.html', 'rb') as file:
            file_data = file.read()
            
        resp_line = "HTTP/1.1 200 OK\r\n"
        resp_header = "Server: PWS1.0\r\n"
        resp_body = file_data

        resp_data = (resp_line + resp_header + "\r\n").encode() + resp_body

        new_socket.send(resp_data)

        # close
        new_socket.close()