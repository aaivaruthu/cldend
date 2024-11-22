import socket

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to an address and port
    server_socket.bind(('localhost', 12345))

    # Listen for incoming connections
    server_socket.listen(1)
    print("Server is listening on port 12345...")

    # Accept a client connection
    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")

    try:
        # Receive message from the client
        message = client_socket.recv(1024).decode()
        print(f"Received from client: {message}")

        # Echo the message back to the client
        client_socket.send(message.encode())
        print(f"Echoed back to client: {message}")
    finally:
        # Close client and server sockets
        client_socket.close()
        server_socket.close()
        print("Server closed.")

if __name__ == "__main__":
    start_server()
