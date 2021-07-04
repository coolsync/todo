import socket


if __name__ == '__main__':
    # 1. create server socket
    ser_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 2. bind ip and port
    ser_socket.bind(("", 8081))

    # 3. listen port
    ser_socket.listen()

    print('Server start ok!')
    # 4. get connect new client
    new_cli, ip_port= ser_socket.accept()
    print('new client addr: ', ip_port)

    # 5. recv data
    recv_data = new_cli.recv(1024)
    recv_con = recv_data.decode('utf-8')

    print('recv client data: ', recv_con)

    # 6. send data
    send_con = 'server say: ' + recv_con
    send_data = send_con.encode()

    new_cli.send(send_data)

    # 7. close client connect
    new_cli.close()

    # 8. close server socket
    ser_socket.close()