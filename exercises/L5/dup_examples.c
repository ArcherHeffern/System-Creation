#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

#define BUFSIZE 1024

int dup_files();
int replace();

int main() {
    printf("1) dup_files\n");
    printf("2) replace stdout with file\n");
    char c = getc(stdin);
    if (c == '1') {
        dup_files();
    } else if (c == '2') {
        replace();
    } else {
        fprintf(stderr, "Not a valid option\n");
    }
}

/*
Create another reference to a file
*/
int dup_files() {
    int f = open("out.txt", O_RDONLY|O_TRUNC|O_CREAT);
    int f2 = dup(f);
    // Now we can write to out.txt using f or f2

    // Now lets say we want f and f2 to not exist in a child process should we fork/exec, we can use fcntl to modify this setting
    fcntl(f, FD_CLOEXEC);
    fcntl(f2, FD_CLOEXEC);
}

/*
Replace stdout with a file
*/
int replace() {
    int f = open("out.txt", O_WRONLY|O_TRUNC|O_CREAT);
    dup2(f, STDOUT_FILENO); // STDERR_FILENO is defined in unistd.c and equals 2

    char buf[BUFSIZE];
    int n;
    while (1) {
        n = read(STDIN_FILENO, buf, BUFSIZE);
        write(STDOUT_FILENO, buf, n);
    }
}