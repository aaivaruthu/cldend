#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>

int main() {
    int parent_to_child[2]; // Pipe for parent-to-child communication
    int child_to_parent[2]; // Pipe for child-to-parent communication
    pid_t pid;
    char parent_message[] = "Hello from parent!";
    char child_response[] = "Hello from child!";
    char read_buffer[100];

    // Create pipes
    if (pipe(parent_to_child) == -1 || pipe(child_to_parent) == -1) {
        perror("Pipe failed");
        exit(1);
    }

    // Fork to create a child process
    pid = fork();

    if (pid < 0) {
        perror("Fork failed");
        exit(1);
    } else if (pid > 0) { // Parent process
        // Close unused ends of the pipes
        close(parent_to_child[0]); // Close reading end of parent-to-child pipe
        close(child_to_parent[1]); // Close writing end of child-to-parent pipe

        // Send message to the child
        write(parent_to_child[1], parent_message, strlen(parent_message) + 1);
        printf("Parent: Sent message to child.\n");

        // Read the response from the child
        read(child_to_parent[0], read_buffer, sizeof(read_buffer));
        printf("Parent: Received response from child: %s\n", read_buffer);

        // Close used ends of the pipes
        close(parent_to_child[1]);
        close(child_to_parent[0]);
    } else { // Child process
        // Close unused ends of the pipes
        close(parent_to_child[1]); // Close writing end of parent-to-child pipe
        close(child_to_parent[0]); // Close reading end of child-to-parent pipe

        // Read the message from the parent
        read(parent_to_child[0], read_buffer, sizeof(read_buffer));
        printf("Child: Received message from parent: %s\n", read_buffer);

        // Send response to the parent
        write(child_to_parent[1], child_response, strlen(child_response) + 1);
        printf("Child: Sent response to parent.\n");

        // Close used ends of the pipes
        close(parent_to_child[0]);
        close(child_to_parent[1]);
    }

    return 0;
}
