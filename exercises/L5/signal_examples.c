#include <stdio.h>
#include <sys/wait.h>
#include <string.h>
#include <unistd.h>
#include <signal.h>
#include <stdlib.h>

void yes();
void yes2();

int main() {
    printf("1) Default Handler Example\n");
    printf("2) Custom Hanlder Example\n");
    char c = getc(stdin);
    if (c == '1') {
        yes();
    } else if (c == '2') {
        yes2();
    } else {
        printf("Invalid option\n");
        exit(1);
    }
}

void yes() {
    /*
    This uses the default behavior of sending sigint to a process, which is to kill it 
    */
    int pid = fork();
    if (pid == 0) {
        while (1) {
            printf("yes\n");
        }
    }
    sleep(1);
    kill(pid, SIGINT);
}

// Signal handler function
void handle_sigint(int sig) {
    printf("Hahaha you can't kill me! %d\n", sig);
}

void yes2() {
    struct sigaction sa;

    // Initialize the sigaction structure
    sa.sa_handler = handle_sigint; // Pointer to the signal handler function
    sigemptyset(&sa.sa_mask); // Initialize the signal set to empty
    sa.sa_flags = 0; // No flags

    // Set up the signal handler for SIGINT
    if (sigaction(SIGINT, &sa, NULL) == -1) {
        perror("sigaction");
        exit(EXIT_FAILURE);
    }

    printf("Waiting for SIGINT (Ctrl+C)...\n");
    // Infinite loop to keep the program running until SIGINT is received
    while (1) {
        sleep(1); // Sleep for 1 second
        printf("Yes\n");
    }
}