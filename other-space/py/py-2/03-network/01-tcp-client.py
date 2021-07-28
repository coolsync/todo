import socket


if __name__ == '__main__':
    # 1. create socket
    # AF_INET: ipv4 ipv6, SOCK_STREAM: tcp
    cli_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. create connect
    cli_socket.connect(('192.168.122.1', 8081))

    # 3. send data
    send_con = 'hello'
    send_data = send_con.encode('utf-8')

    cli_socket.send(send_data)

    # 4. recv data
    recv_data = cli_socket.recv(1024)
    recv_con = recv_data.decode()
    print(recv_con)
    
    # 5. close 
    cli_socket.close()