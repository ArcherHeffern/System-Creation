#include <sys/types.h>
#include <ctype.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netinet/ip.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define BUFSIZE 1024

struct sockaddr_in* create_empty_socket_address();
struct sockaddr_in* create_socket_address(in_addr_t ip_address, int port);
void stou(char* s);

int main() {
    int s = socket(AF_INET, SOCK_STREAM, 0);

    // Binding to port and ip address
    struct sockaddr_in *local_addr = create_socket_address(INADDR_LOOPBACK, 8080);
    int res = bind(s, local_addr, sizeof(*local_addr));

    // Start listening for connections
    listen(s, 5);


    // ... and accept 1 connection
    struct sockaddr_in *remote_addr = create_empty_socket_address();
    int remote_addr_len = sizeof(remote_addr);
    int remote = accept(s, &remote_addr, &remote_addr_len);

    // Read its input, and YELL it back
    char buffer[BUFSIZE];
    int n = read(remote, buffer, BUFSIZE - 1);
    buffer[n] = 0;
    stou(buffer);
    write(remote, buffer, n);
    shutdown(n, SHUT_RDWR);
    close(s);
}


struct sockaddr_in* create_empty_socket_address() {
    struct sockaddr_in *sock = (struct sockaddr_in *) malloc(sizeof(struct sockaddr_in));
    memset(sock, 0, sizeof(struct sockaddr_in));
    return sock;
}

struct sockaddr_in* create_socket_address(in_addr_t ip_address, int port) {
    struct sockaddr_in* sock = create_empty_socket_address();
    sock->sin_family = AF_INET;
    sock->sin_port = htons(port);
    sock->sin_addr.s_addr = htonl(ip_address);
    return sock;
}

// String to Uppercase
void stou(char* s) {
    while (*s) {
        *s = toupper(*s);
        s++;
    }
}