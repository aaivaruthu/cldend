import socket
import json

def send_request(function, args, host='127.0.0.1', port=65432):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Prepare the request data in JSON format
    request = {
        "function": function,
        "args": args
    }
    client_socket.sendall(json.dumps(request).encode())

    # Receive the response from the server
    response = client_socket.recv(1024).decode()
    result = json.loads(response).get("result")
    print(f"Result: {result}")

    client_socket.close()

if __name__ == "__main__":
    print("Available functions: add, subtract, multiply, divide")
    function = input("Enter function name: ")
    args = input("Enter arguments (comma-separated): ").split(",")

    # Convert arguments to integers or floats as needed
    args = [float(arg) if '.' in arg else int(arg) for arg in args]

    send_request(function, args)
