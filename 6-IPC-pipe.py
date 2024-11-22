from multiprocessing import Process, Pipe

def parent_process(parent_conn, child_conn):
    # Close the child end of the pipe in the parent
    child_conn.close()
    
    # Send a message to the child
    parent_message = "Hello from parent!"
    parent_conn.send(parent_message)
    print("Parent: Sent message to child.")

    # Receive the response from the child
    child_response = parent_conn.recv()
    print("Parent: Received response from child:", child_response)
    
    # Close the parent end of the pipe
    parent_conn.close()

def child_process(parent_conn, child_conn):
    # Close the parent end of the pipe in the child
    parent_conn.close()
    
    # Receive the message from the parent
    parent_message = child_conn.recv()
    print("Child: Received message from parent:", parent_message)

    # Send a response back to the parent
    child_message = "Hello from child!"
    child_conn.send(child_message)
    print("Child: Sent response to parent.")
    
    # Close the child end of the pipe
    child_conn.close()

if __name__ == "__main__":
    # Create a duplex pipe for bidirectional communication
    parent_conn, child_conn = Pipe()

    # Create the child process
    child = Process(target=child_process, args=(parent_conn, child_conn))
    child.start()

    # Run the parent process logic
    parent_process(parent_conn, child_conn)

    # Wait for the child process to complete
    child.join()
