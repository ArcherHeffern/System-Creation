#include <sys/types.h>
#include <unistd.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h> 
#include <stdlib.h>

#define ERR_NOT_ENOUGH_ARGUMENTS 1
#define BUFSIZE 1024

int main(int argc, char** argv) {
    if (argc < 2) {
        printf("Not enough arguments\n");
        exit(ERR_NOT_ENOUGH_ARGUMENTS);
    }
    int f = open(argv[1], O_RDONLY);
    int n = 1;
    char buf[BUFSIZE];
    while (n > 0) {
        n = read(f, buf, BUFSIZE - 1);
        buf[n] = 0;
        write(1, buf, BUFSIZE);
    }
    if (n < 0) {
        fprintf(stderr, "Erorr reading file\n");
    }
}