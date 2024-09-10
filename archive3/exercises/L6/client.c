#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <stdio.h>
#include <netinet/in.h>
#include <netinet/ip.h>
#include <stdlib.h>
#include <string.h>
#include <arpa/inet.h>

#define CHECK(expr) if ((expr) == -1) { perror("Check"); exit(1); }

struct sockaddr_in* create_empty_socket_address();
struct sockaddr_in* create_socket_address(in_addr_t ip_address, int port);

int main() {
    printf("What is the remote port: ");
    int port;
    scanf("%d", &port);

    // Create socket
    int s = socket(AF_INET, SOCK_STREAM, 0);
    CHECK(s);

    // Create remote address
    struct sockaddr_in *remote_addr = create_socket_address(inet_addr("127.0.0.1"), htons(port));

    // Connect to remote
    int connect_result = connect(s, (struct sockaddr *) remote_addr, sizeof(struct sockaddr_in));
    CHECK(connect_result);

    // Write to remote
    const char *message = "Hello world\n";
    ssize_t write_result = write(s, message, strlen(message));
    CHECK(write_result);

    printf("Message sent\n");

    close(s);
    free(remote_addr);
}

struct sockaddr_in* create_empty_socket_address() {
    struct sockaddr_in *sock = (struct sockaddr_in *) malloc(sizeof(struct sockaddr_in));
    memset(sock, 0, sizeof(struct sockaddr_in));
    return sock;
}

struct sockaddr_in* create_socket_address(in_addr_t ip_address, int port) {
    struct sockaddr_in* sock = create_empty_socket_address();
    sock->sin_family = AF_INET;
    sock->sin_port = port;
    sock->sin_addr.s_addr = ip_address;
    return sock;
}