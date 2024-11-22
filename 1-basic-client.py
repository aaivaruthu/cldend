import socket

def start_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect(('localhost', 12345))

    # Send a message to the server
    message = "Hello, Server!"
    client_socket.send(message.encode())
    print(f"Sent to server: {message}")

    # Receive the echoed message from the server
    echoed_message = client_socket.recv(1024).decode()
    print(f"Received from server: {echoed_message}")

    # Close the socket
    client_socket.close()
    print("Client closed.")

if __name__ == "__main__":
    start_client()
