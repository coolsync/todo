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

        if recv_con.find('GET') != 0:
            print(f'close {ip_port} clinet')
            new_socket.close()
            return

        # recv_con.split(' ', maxsplit=2)
        recv_list = recv_con.split(' ', 2)
        # print(recv_list[1])

        req_path = recv_list[1]
        if req_path == '/':
            req_path = '/index.html'

        # page not exists, return error page 
        try:
            # send data to client
            with open('static' + req_path, 'rb') as file:
                file_data = file.read()

        except Exception as e:
            with open('static/' + 'error.html', 'rb') as file:
                file_data = file.read()

            resp_line = "HTTP/1.1 404 Not Found\r\n"
            resp_header = "Server: PWS1.0\r\n"
            resp_body = file_data

            resp_data = (resp_line + resp_header + "\r\n").encode() + resp_body

            new_socket.send(resp_data)

        else:
            resp_line = "HTTP/1.1 200 OK\r\n"
            resp_header = "Server: PWS1.0\r\n"
            resp_body = file_data

            resp_data = (resp_line + resp_header + "\r\n").encode() + resp_body

            new_socket.send(resp_data)

        finally:
            # close
            new_socket.close()


if __name__ == '__main__':
    main()
