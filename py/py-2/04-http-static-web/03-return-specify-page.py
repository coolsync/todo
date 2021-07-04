import socket


def main():
    # create server
    ser_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    ser_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    ser_socket.bind(("", 8081))

    ser_socket.listen(128)

    while True:
        # read recv data
        new_socket, ip_port = ser_socket.accept()

        recv_data = new_socket.recv(4096)

        if len(recv_data) == 0:
            print('close this clinet')
            new_socket.close()
            return

        print(recv_data)
        recv_con = recv_data.decode('utf-8')
        
        # recv_con.split(' ', maxsplit=2)
        recv_list = recv_con.split(' ', 2)
        print(recv_list[1])
        
        if len(recv_list) == 0:
            print('close this clinet')
            new_socket.close()
            return
        
        static_data = recv_list[1]
        if static_data == '/':
            static_data = '/index.html'

        # send data to client
        with open('static' + static_data, 'rb') as file:
            file_data = file.read()

        resp_line = "HTTP/1.1 200 OK\r\n"
        resp_header = "Server: PWS1.0\r\n"
        resp_body = file_data

        resp_data = (resp_line + resp_header + "\r\n").encode() + resp_body

        new_socket.send(resp_data)

        # close
        new_socket.close()


if __name__ == '__main__':
    main()
