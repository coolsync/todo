import socket
import threading
import sys

class WebServer(object):

    def __init__(self, post) -> None:
        # create server
        ser_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        ser_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

        ser_socket.bind(("", post))

        ser_socket.listen(128)

        self.ser_socket = ser_socket


    @staticmethod
    def handle_client(new_socket, ip_port):
        print(f'{ip_port} client connect ok!')

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


    def start(self):
        while True:
            # read recv data
            new_socket, ip_port = self.ser_socket.accept()
            # print(f'{ip_port} server start ok!')

            # for every client create single thread
            t1 = threading.Thread(target=self.handle_client,
                                  args=(new_socket, ip_port))
            t1.setDaemon(True)
            t1.start()


def main():
    print(sys.argv)
    # command params len != 2
    if len(sys.argv) != 2:
        print('form like: python name.py 8000')
        return

    # command params is not digit
    if not sys.argv[1].isdigit():
        print('form like: python name.py 8000')
        return
    
    port = int(sys.argv[1])
    
    # create server object
    web_srv = WebServer(port)

    web_srv.start()

if __name__ == '__main__':
    main()
