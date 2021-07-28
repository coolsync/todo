import socket
import threading

def handle_client(new_cli, ip_port):
    print('new client addr: ', ip_port)
    while True:
        # 5. recv data
        recv_data = new_cli.recv(1024)

        if recv_data:
            recv_con = recv_data.decode('utf-8')
            print('data size: %d' % len(recv_data))
            print('recv client data: %s' % recv_con)

            # 6. send data
            send_data = 'server say: ' + recv_con
            new_cli.send(send_data.encode())
        else:
            print('client offline: ', ip_port)
            break

    # 7. close client connect
    new_cli.close()


if __name__ == '__main__':
    # 1. create server socket
    ser_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # set port numbr multiplexing
    # SOL_SOCKET:   Indicates the current socket
    # SO_REUSEADDR: Set port number multiplexing options
    # True: Set the value corresponding to the port number multiplexing option
    ser_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    # 2. bind ip and port, "": all local host ip
    ser_socket.bind(("", 8081))

    # 3. listen port
    ser_socket.listen()
    print('Server start ok!')

    while True:
        # 4. get connect new client
        new_cli, ip_port = ser_socket.accept()

        sub_thread = threading.Thread(target=handle_client, args=(new_cli, ip_port))
        sub_thread.setDaemon(True)  # 守护主线程: 主线程退出 子线程销毁 不再执行
        sub_thread.start()

    # 8. close server socket
    # ser_socket.close()
