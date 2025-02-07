#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

#define EXT_SUCCESS 0
#define EXT_ERR_EXEC 1

int main(int argc, char** argv, char** envp) {
    printf("Starting Program...\n");
    printf("See execve(2) or execl(3) for its varients!\n\n");
    int stat_loc;
    char *args[] = {" ", 0};
    if (fork() == 0) {
        printf("Running ls using absolute path (/bin/ls)\n");
        if (execve("/bin/ls", args, envp) == -1) {
            perror("Executing program");
            exit(EXT_ERR_EXEC);
        }
    }
    wait(&stat_loc);
    if (fork() == 0) {
        printf("\n\nRunning a program using relative path (./helper)\n");
        if (execve("./helper", args, envp) == -1) {
            perror("Executing program");
            exit(EXT_ERR_EXEC);
        }
    }
    wait(&stat_loc);
    if (fork() == 0) {
        // I quite like using the frontends with p in them because they will checks the (p)ath variable for commands. Notice how we don't have to specify an absolute or relative path here. 
        printf("\n\nRunning ls using path variable and execvp (ls)\n");
        if (execvp("ls", args) == -1) {
            perror("Executing program");
            exit(EXT_ERR_EXEC);
        }
    }
    wait(&stat_loc);
    printf("Done!\n");
    exit(EXT_SUCCESS);
}