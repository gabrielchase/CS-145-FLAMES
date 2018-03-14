import socket

QUIT = 'quit'
RECEIVED = 'received'


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.1.6', 58913))

while True:
    data = raw_input('input ')
    assert isinstance(data, basestring)

    client_socket.send(data)
    server_response = client_socket.recv(64)
    
    while server_response not in [RECEIVED, QUIT]:
        continue

    if server_response == RECEIVED:
        print('--- Server received {} ---'.format(data))

    if server_response == QUIT:
        print('--- Server closed connection ---')
        client_socket.close()
        break
    
    print('')

client_socket.close()
