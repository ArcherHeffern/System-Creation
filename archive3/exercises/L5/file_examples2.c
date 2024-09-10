#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>

#define ERR_OPEN 1
#define ERR_WRITE 2
#define ERR_CLOSE 3
#define OUTFILE "out.txt"

/*
Warning: There is minimal error handling in this program
*/

int main() {
    char* buf = "Hello world\n";
    int size = strlen(buf);
    int f;
    if ((f = open(OUTFILE, O_CREAT|O_RDWR|O_TRUNC, 0644)) == -1) {
        perror("Open");
        exit(ERR_OPEN);
    }

    int total_written = 0;
    while (total_written < size) {
        int n;
        if ((n = write(f, buf + total_written, size - total_written)) == -1) {
            perror("Writing");
            exit(ERR_WRITE);
        }
        total_written += n;
    }

    if (close(f) == -1) {
        perror("Close");
        exit(ERR_CLOSE);
    }
}