#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <unistd.h>
#include <errno.h>
#include "utils.h"
#include "sockutils.h"

#define BUFLEN 255

int main(int argc, char **argv) {
    struct addrinfo *info;
    char *request = "GET / HTTP/1.1\r\n\r\n";
    char response[BUFLEN];
    int host, n;

    if(argc != 3)
        die("Usage: %s server port\n", argv[0]);
    info = make_addrinfo(argv[1], argv[2]);
    
    if((host = host_connect(info)) < 0)
        pdie("host_connect");

    memset(response, 0, BUFLEN);

    // This improves dumbfetch by checking for errors from read and
    // handling arbitrarily long responses from the server (using
    // a loop that calls read() as many times as necessary).
    //
    // Note that we still haven't handled the "short write" problem
    // or checked for errors from the call to write(). Your code will
    // have to deal with those situations!
    
    write(host, request, strlen(request)); // could still have short writes!
    while((n = read(host, response, BUFLEN)) > 0)
        printf("%s", response);
    if(n < 0)
        pdie("read");

    close(host);      
    free_addrinfo(info);
    
    return 0;
}
