import socket
import json

# Define functions the server can perform
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b if b != 0 else "Error: Division by zero"

# Dictionary to map function names to actual functions
functions = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide
}

def start_server(host='127.0.0.1', port=65432):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Server is listening for connections...")

    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    while True:
        # Receive request from the client
        data = conn.recv(1024).decode()
        if not data:
            break

        # Parse JSON request
        request = json.loads(data)
        func_name = request.get("function")
        args = request.get("args", [])

        # Execute the requested function
        if func_name in functions:
            try:
                result = functions[func_name](*args)
            except Exception as e:
                result = f"Error: {e}"
        else:
            result = f"Error: Unknown function '{func_name}'"

        # Send the result back to the client
        response = json.dumps({"result": result})
        conn.sendall(response.encode())

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
