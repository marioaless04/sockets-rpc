import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    mensaje = input("Ingrese un mensaje para enviar al servidor: ")
    client.sendall(mensaje.encode())
    data = client.recv(1024).decode()
    print("Respuesta del servidor:", data)
