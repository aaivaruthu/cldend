import socket

def send_file(filename, host='127.0.0.1', port=65432):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Open the file and send its contents
    with open(filename, "rb") as file:
        while chunk := file.read(1024):
            client_socket.sendall(chunk)  # Send data in chunks

    print(f"File '{filename}' sent to server.")
    client_socket.close()

if __name__ == "__main__":
    filename = "abc.txt"  # Replace with your file path
    send_file(filename)
