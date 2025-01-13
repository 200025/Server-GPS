import socket

# Configurare server
HOST = "0.0.0.0"  # Ascultă pe toate interfețele
PORT = 8080       # Portul pe care îl alegi

# Creează un socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)  # Maxim 5 conexiuni în coadă
print(f"Server running on port {PORT}...")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    # Primește date
    data = client_socket.recv(1024).decode()
    print(f"Received data: {data}")

    # Trimite răspuns (opțional)
    client_socket.sendall(b"Data received successfully!")

    # Închide conexiunea cu clientul
    client_socket.close()
