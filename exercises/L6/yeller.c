#include <sys/types.h>
#include <unistd.h>
#include <ctype.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netinet/ip.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define BUFSIZE 1024

#define ERR_SOCKET 1
#define ERR_BIND 2
#define ERR_ACCEPT 3

void stou(char* s);

int main() {
    int s;
    if ((s = socket(AF_INET, SOCK_STREAM, 0)) == -1) {
        perror("Socket");
        exit(ERR_SOCKET);
    }

    // Binding to port and ip address
    struct sockaddr_in sock;
    memset(&sock, 0, sizeof sock);
    sock.sin_family = AF_INET;
    sock.sin_port = htons(8080);
    sock.sin_addr.s_addr = htonl(INADDR_LOOPBACK);
    if (bind(s, (struct sockaddr_in *) &sock, sizeof(sock)) == -1) {
        perror("Bind");
        exit(ERR_BIND);
    }

    // Start listening for connections
    listen(s, 5);

    struct sockaddr_in s_acc;
    memset(&s_acc, 0, sizeof s_acc);
    int s_acc_size = sizeof s_acc;
    int remote;

    // ... and accept 1 connection
    if ((remote = accept(s, (struct sockaddr_in *)&s_acc, &s_acc_size)) == -1) {
        perror("Accept");
        exit(ERR_ACCEPT);
    }

    // Read its input, and YELL it back
    char buffer[BUFSIZE];
    int n = read(remote, buffer, BUFSIZE - 1);
    buffer[n] = 0;
    stou(buffer);
    write(remote, buffer, n);
    shutdown(n, SHUT_RDWR);
    close(s);
}

// String to Uppercase
void stou(char* s) {
    while (*s) {
        *s = toupper(*s);
        s++;
    }
}