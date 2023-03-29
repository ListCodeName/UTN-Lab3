import socket

server = socket.socket(family = socket.AF_INET, type=socket.SOCK_STREAM)
server.bind(("0.0.0.0",8080))

server.listen(2)

while True:
    connection, address = server.accept()
    while True:
            data = connection.recv(1024)
            print('received {0}'.format(data))
            if data:
                print('Enviando de regreso los dato al cliente ')
                connection.sendall(data)
            else:
                print('no hay mas datos de', address)
                break
