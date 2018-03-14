from __future__ import print_function
import socket

QUIT = 'quit'
QUIT_TRIGGER = 'q'
RECEIVED = 'received'


def start_server():
    while True:
        data = conn.recv(64)
        if data == QUIT_TRIGGER:
            print('--- Closing connection ---')
            conn.send(QUIT)
            conn.close()
            break
        else:
            print('DATA: {}'.format(data))
            conn.send(RECEIVED)



if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', 58913))
    server_socket.listen(5) 
    conn, _ = server_socket.accept()

    start_server()

    server_socket.close()

