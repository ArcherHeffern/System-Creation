#include <sys/types.h>
#include <unistd.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h> 
#include <stdlib.h>

#define ERR_NOT_ENOUGH_ARGUMENTS 1
#define ERR_READ 2
#define ERR_CLOSE 3
#define BUFSIZE 1024

int main(int argc, char** argv) {
    if (argc < 2) {
        fprintf(stderr, "Not enough arguments\n");
        exit(ERR_NOT_ENOUGH_ARGUMENTS);
    }
    int f = open(argv[1], O_RDONLY);
    int n = 1;
    char buf[BUFSIZE];
    while (n > 0) {
        n = read(f, buf, BUFSIZE - 1);
        if (n < 0) {
            perror("Read");
            exit(ERR_READ);
        }
        buf[n] = 0;
        write(1, buf, BUFSIZE); // My goodness, what does this mean? 
    }
    if (close(f) == -1) {
        perror("Close");
        exit(ERR_CLOSE);
    }
}