from __future__ import print_function
import socket
import collections

QUIT = 'quit'
QUIT_TRIGGER = 'q'
RECEIVED = 'received'
FLAMES = 'FLAMES'
FLAMES_DICT = {
    'F': 'Friendship',
    'L': 'Love',
    'A': 'Affection',
    'M': 'Marriage',
    'E': 'Enemy',
    'S': 'Sibling'
}
HOST = 55551


def get_flames_count(data):
    split_data = data.split(',')
    w1 = collections.Counter(split_data[0])
    w2 = collections.Counter(split_data[1])
    unique_letters_list = list((w1 - w2).elements()) + list((w2 - w1).elements())
    unique_letters = ''.join(unique_letters_list).strip().replace(' ', '')

    print('Unique Letters: {}'.format(unique_letters))
    return len(unique_letters)

def get_relationship(flames_count, current_idx=0, current_flames=FLAMES):
    if len(current_flames) == 1:
        return FLAMES_DICT.get(current_flames)
    else:
        current_idx = (current_idx + flames_count - 1) % len(current_flames)
        current_flames = current_flames[:current_idx] + current_flames[current_idx + 1:]

        return get_relationship(flames_count, current_idx, current_flames)

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
            relationship = get_relationship(flames_count=flames_count)
            
            print('flames_count: {}'.format(flames_count))
            print('relationship: {}\n'.format(relationship))
            
            conn.send(RECEIVED)



if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', HOST))
    server_socket.listen(5) 
    conn, _ = server_socket.accept()

    start_server()

    server_socket.close()
