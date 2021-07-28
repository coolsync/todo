
# import module
import socket

if __name__ == '__main__':
    # create socket
    cli_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    visit_site = 'hlw1.live'
    # create connect
    cli_socket.connect((visit_site, 80))

    # send req msg to ser
    req_line = 'GET / HTTP/1.1\r\n'

    req_header = 'Host: '+visit_site+'\r\n'

    req_blank = '\r\n\r\n'

    req_msg = req_line + req_header + req_blank

    cli_socket.send(req_msg.encode())

    # recv server res msg
    recv_data = cli_socket.recv(40960)

    recv_text = recv_data.decode()

    index = recv_text.find('\r\n\r\n')

    html_data = recv_text[index+4:]
    # save file
    with open('index.html', 'w') as file:
        file.write(html_data)

    # close
    cli_socket.close()
