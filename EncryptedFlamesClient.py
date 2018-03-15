from EncryptedFlamesServer import (
    HOST, SHIFT_KEY, caesar_cipher_encrypt, caesar_cipher_decrypt
)
import socket

QUIT = 'quit'
RECEIVED = 'received'
FLAMES_VALUES = ['Friendship', 'Love', 'Affection', 'Marriage', 'Enemy', 'Sibling']
ALLOWED_RESPONSES = FLAMES_VALUES + [QUIT]
LETTERS_IN_ALPHABET = 26


def start_client():
    while True:
        data = raw_input('input ')
        assert isinstance(data, basestring)

        encrypted_data = caesar_cipher_encrypt(data)
        client_socket.send(encrypted_data)
        server_response = client_socket.recv(64)
        decrypted_server_response = caesar_cipher_decrypt(server_response, SHIFT_KEY).title()
        
        while decrypted_server_response not in ALLOWED_RESPONSES:
            continue

        if decrypted_server_response in FLAMES_VALUES:
            print(decrypted_server_response)

        if decrypted_server_response == QUIT:
            print('--- Server closed connection ---')
            client_socket.close()
            break
        
        print('')


if __name__ == '__main__':
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', HOST))

    start_client()

    client_socket.close()
