
import socket

# Configuración del cliente
host = '127.0.0.1'
port = 8080

# Creación del socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conexión al servidor
client_socket.connect((host, port))

# Envío de datos al servidor
message = "Hola, servidor echo!"
client_socket.sendall(message.encode())

# Recepción de datos del servidor
data = client_socket.recv(1024)

# Decodificación de los datos recibidos y muestra del resultado
print(f"Datos recibidos del servidor: {data.decode()}")

# Cierre del socket
client_socket.close()