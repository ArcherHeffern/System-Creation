#include <unistd.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

#define ERR_PIPE 1
#define ERR_FORK 2

#define BUFSIZE 1024

/*
Note: There is very minimal error handling in this program for ease of reading
*/
void process_child(int p_read);
void process_parent(int p_write);

int main() {
    int pipe_fd[2];
    if (pipe(pipe_fd) == -1) {
        perror("Pipe");
        exit(ERR_PIPE);
    }

    int p_read = pipe_fd[0];
    int p_write = pipe_fd[1];

    int pid = fork();
    if (pid == 0) {
        process_child(p_read);
        exit(0);
    } else if (pid > 0) {
        process_parent(p_write);
    } else {
        fprintf(stderr, "Error creating pipe\n");
        exit(ERR_FORK);
    }
}

void process_child(int p_read) {
    char buf[BUFSIZE];
    int n = read(p_read, buf, BUFSIZE - 1);
    buf[n] = 0;
    printf("%s\n", buf);
}

void process_parent(int p_write) {
    char *msg = "Hello from parent process!!!";
    write(p_write, msg, strlen(msg));
}