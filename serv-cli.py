"""
Conectarse al servidor meteorológico Galileo Galilei y obtener los datos que el cliente solicita.
Efectuada una consulta, no se pueden hacer peticiones al servidor durante 5 minutos.
"""

import socket
import threading
import requests
from datetime import datetime

#Tiempo de la ultima petición y ultima medición obtenida

def cliente():
    # Configuración del cliente
    host = socket.gethostname()
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
        client_socket.sendall(message.encode("UTF-8"))


        # Recepción de datos del servidor
        data = client_socket.recv(1024)
        # Decodificación de los datos recibidos y muestra del resultado
        print(f"Datos recibidos del servidor: {data.decode()}")


        # Cierre del socket
        if message == "exit":
            print("Finalizando sesión cliente.")
            client_socket.close()
            break

def servidor():
    server = socket.socket(family = socket.AF_INET, type=socket.SOCK_STREAM)
    server.bind((socket.gethostname(),8080))

    last = None
    server.listen(2)
    data = None

    while True:
        connection, address = server.accept()
        while True:
                data = connection.recv(1024).decode("UTF-8")
                if(format(data) != ""):
                    last = format(data)
                #print('Entry: {0}'.format(data))
                if data:
                    connection.sendall(consultaTiempo(format(data)).encode("UTF-8"))
                else:
                    break
        if last=="exit":
            print("Finalizando sesión servidor.")
            break

def consultaTiempo(texto):
    respuesta = ""
    valor = 0
    try:
        valor = datetime.now()-int(str(lastRequest).split(":")[1])
    except:
        valor = 10
    if valor > 5:
        if(texto == "clima"):
            lastRequest = datetime.now()
            medicion = galileoReq()
            respuesta = "\nUltima medición "+str(medicion[0])+" a las "+str(medicion[1])+" hrs  \nLa temperatura actual es: " + str(medicion[2]) +"ºC"
        else:
            respuesta = "El servidor no reconoce su petición."
    else:
        respuesta = "El tiempo transcurrido desde la ultima consulta es menor a 5 minutos."
    return respuesta

def galileoReq():
    req = requests.get('https://www.frcon.utn.edu.ar/galileo/downld02.txt')
    aux = req.text.split("\r\n")
    return aux[len(aux)-2].split()

lastRequest = datetime.now()
medicion = ""

# creamos el hilo del servidor y ejecutamos
servThread = threading.Timer(1,function=servidor)
servThread.start() 

# creamos el hilo del cliente y ejecutamos
cliThread = threading.Timer(1, function=cliente)
cliThread.start()