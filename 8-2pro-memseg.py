import multiprocessing
import time

def writer(shared_memory):
    # Write a message into shared memory
    message = b"Hello from the writer process!"
    shared_memory[:len(message)] = message
    print("Writer: Data written to shared memory.")
    
    # Sleep to simulate some processing time
    time.sleep(2)

def reader(shared_memory):
    # Sleep to give the writer time to write data
    time.sleep(1)
    
    # Read the message from shared memory
    message = bytes(shared_memory[:]).rstrip(b'\x00').decode('utf-8')
    print("Reader: Data read from shared memory:", message)

def main():
    # Create a shared memory block with a size of 1024 bytes
    shared_memory = multiprocessing.Array('b', 1024)

    # Create two processes: writer and reader
    writer_process = multiprocessing.Process(target=writer, args=(shared_memory,))
    reader_process = multiprocessing.Process(target=reader, args=(shared_memory,))

    # Start the processes
    writer_process.start()
    reader_process.start()

    # Wait for both processes to finish
    writer_process.join()
    reader_process.join()

if __name__ == "__main__":
    main()
