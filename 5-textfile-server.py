import socket

def start_server(host='127.0.0.1', port=65432):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Server is listening for connections...")

    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    # Open a file to save the incoming data
    with open("received_file.txt", "wb") as file:
        while True:
            # Receive data in chunks
            data = conn.recv(1024)
            if not data:
                break
            file.write(data)  # Write data to file
    print("File received and saved as 'received_file.txt'.")

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
