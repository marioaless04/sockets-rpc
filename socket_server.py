import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    print(f"Servidor escuchando en {HOST}:{PORT}")
    conn, addr = server.accept()
    with conn:
        print('Conexión establecida desde', addr)
        data = conn.recv(1024).decode()
        print("Mensaje recibido:", data)
        conn.sendall("Mensaje recibido con éxito".encode())
