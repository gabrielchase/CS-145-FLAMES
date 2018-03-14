from __future__ import print_function
import socket
import collections

QUIT = 'quit'
QUIT_TRIGGER = 'q'
RECEIVED = 'received'
HOST = 55554


def get_flames_count(data):
    split_data = data.split(',')
    w1 = collections.Counter(split_data[0])
    w2 = collections.Counter(split_data[1])
    
    unique_letters_list = list((w1 - w2).elements()) + list((w2 - w1).elements())
    unique_letters = ''.join(unique_letters_list).strip()

    print('Unique Letters: ', unique_letters)
    return len(unique_letters)

def start_server():
    while True:
        data = conn.recv(64)
        if data == QUIT_TRIGGER:
            print('--- Closing connection ---')
            conn.send(QUIT)
            conn.close()
            break
        else:
            flames_count = get_flames_count(data)
            print('flames_count: {}\n'.format(flames_count))
            conn.send(RECEIVED)



if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', HOST))
    server_socket.listen(5) 
    conn, _ = server_socket.accept()

    start_server()

    server_socket.close()

