#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <netinet/ip.h>
#include <sys/socket.h>
#include <arpa/inet.h>

#define PACKET_LEN 512

// Function to calculate the checksum
unsigned short checksum(void *b, int len) {    
    unsigned short *buf = b;
    unsigned int sum = 0;
    unsigned short result;

    for (sum = 0; len > 1; len -= 2)
        sum += *buf++;
    if (len == 1)
        sum += *(unsigned char *)buf;
    sum = (sum >> 16) + (sum & 0xFFFF);
    sum += (sum >> 16);
    result = ~sum;
    return result;
}

int main(int argc, char *argv[]) {
    int sockfd;
    struct sockaddr_in dest;
    char packet[PACKET_LEN];
    struct iphdr *ip_header = (struct iphdr *) packet;
    int one = 1;
    const int *val = &one;

    // Create a raw socket
    sockfd = socket(AF_INET, SOCK_RAW, IPPROTO_RAW);
    if (sockfd < 0) {
        perror("socket");
        return 1;
    }

    // Set IP_HDRINCL option
    if (setsockopt(sockfd, IPPROTO_IP, IP_HDRINCL, val, sizeof(one)) < 0) {
        perror("setsockopt");
        return 1;
    }

    // Destination address
    dest.sin_family = AF_INET;
    dest.sin_port = 0; // Not used
    dest.sin_addr.s_addr = inet_addr("127.0.0.1"); // Change this to destination IP address

    // Fill in the IP header
    ip_header->ihl = 5;
    ip_header->version = 4;
    ip_header->tos = 0;
    ip_header->tot_len = sizeof(struct iphdr);
    ip_header->id = htons(54321); // Id of this packet
    ip_header->frag_off = htons(0);
    ip_header->ttl = 255;
    ip_header->protocol = IPPROTO_RAW; // Set protocol to raw
    ip_header->check = 0; // Set to 0 before calculating checksum
    ip_header->saddr = inet_addr("1.2.3.4"); // Change this to source IP address
    ip_header->daddr = dest.sin_addr.s_addr;

    // Calculate the IP header checksum
    ip_header->check = checksum(ip_header, sizeof(struct iphdr));

    // Send the packet
    if (sendto(sockfd, packet, sizeof(struct iphdr), 0, (struct sockaddr *)&dest, sizeof(dest)) < 0) {
        perror("sendto");
        return 1;
    }

    close(sockfd);
    return 0;
}