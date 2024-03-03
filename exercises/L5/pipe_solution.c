#include <unistd.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

#define ERR_PIPE 1
#define ERR_FORK 2

#define BUFSIZE 1024

/*
Note: There is very minimal error handling in this program for ease of reading
*/
void process_child(int p_read, int p_write);
void process_parent(int p_read, int p_write);

int main() {
    int pipe_fd1[2];
    int pipe_fd2[2];
    if (pipe(pipe_fd1) == -1) {
        perror("Pipe");
        exit(ERR_PIPE);
    }
    if (pipe(pipe_fd2) == -1) {
        perror("Pipe");
        exit(ERR_PIPE);
    }

    int p_read1 = pipe_fd1[0];
    int p_write1 = pipe_fd1[1];

    int p_read2 = pipe_fd2[0];
    int p_write2 = pipe_fd2[1];

    int pid = fork();
    if (pid == 0) {
        process_child(p_read1, p_write2);
        exit(0);
    } else if (pid > 0) {
        process_parent(p_read2, p_write1);
    } else {
        fprintf(stderr, "Error creating pipe\n");
        exit(ERR_FORK);
    }
}

void process_child(int p_read, int p_write) {
    char buf[BUFSIZE];
    int n = read(p_read, buf, BUFSIZE - 1);
    buf[n] = 0;
    char *p = buf;
    while (*p) {
        *p = toupper(*p);
        p++;
    }
    write(p_write, buf, n);
}

void process_parent(int p_read, int p_write) {
    char *msg = "shout";
    write(p_write, msg, strlen(msg));
    char buf[BUFSIZE];
    int n = read(p_read, buf, BUFSIZE - 1);
    buf[n] = 0;
    printf("%s\n", buf);
}