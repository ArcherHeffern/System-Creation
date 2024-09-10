#include <unistd.h>

/*
Swap stdout and stderr
*/
int main() {
    int stderr_tmp = dup(STDERR_FILENO); // STDERR_FILENO is defined in unistd.c and equals 2
    dup2(STDOUT_FILENO, STDERR_FILENO);
    dup2(stderr_tmp, STDOUT_FILENO);
    close(stderr_tmp); // This just closes the descriptor, not the file it references
}