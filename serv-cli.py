"""
Conectarse al servidor meteorológico Galileo Galilei y obtener los datos que el cliente solicita.
"""

import socket
import threading

def cliente():
    # Configuración del cliente
    host = '192.168.1.6'
    port = 8080
    print("***Bienvenido al sistema de atención meteorológica***")
    while True:
        # Creación del socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Conexión al servidor
        client_socket.connect((host, port))
        # Envío de datos al servidor
        print("**Comandos**\nclima - Obtiene la temperatura actual.\nexit - Cierra el programa.")
        message = input("Escriba un comando: ")
        client_socket.sendall(message.encode())


        # Recepción de datos del servidor
        data = client_socket.recv(1024)
        # Decodificación de los datos recibidos y muestra del resultado
        print(f"Datos recibidos del servidor: {data.decode()}")


        # Cierre del socket
        if message == "exit":
            client_socket.close()

def servidor():
    server = socket.socket(family = socket.AF_INET, type=socket.SOCK_STREAM)
    server.bind(("192.168.1.6",8080))

    server.listen(2)


    while True:
        connection, address = server.accept()
        while True:
                data = connection.recv(1024)
                #print('Entry: {0}'.format(data))
                if data:
                    print('Enviando de regreso los dato al cliente')
                    connection.sendall(data)
                else:
                    print('No hay mas datos de', address)
                    break

# creamos el hilo del servidor y ejecutamos
servThread = threading.Timer(1,function=servidor)
servThread.start() 

# creamos el hilo del cliente y ejecutamos
cliThread = threading.Timer(1, function=cliente)
cliThread.start()