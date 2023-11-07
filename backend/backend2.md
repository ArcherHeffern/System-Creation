osint and google search 

N/A: Things to think about from the reading: 
* How does TCP provide reliability dispite using an unreliable protocol (IP)?
* How is a message built up on each layer? Draw this out

Recap: 
* Protocol: It is an agreement between multiple parties as to how communication will be facilitated
    In the reading, you 
* Internet as layers of protocols
    * What are the major layers?
* IP, TCP, and UDP, draw out their relationship

Practice: Example of message going through the layers and structure of a message as going through the layers

*visualize with wireshark*

## Practice with implementing a protocol on top of TCP
*See mail protocol*
Note: A protocol is a specification (think document), it is up to the programmer how exactly to implement it 

## Tech Recap
* Sockets: Most basic way for you to access the network, is provided by your operating system. Allows you to send TCP, UDP, and IP messages and access lower abstractions with "raw sockets". Every major programming language should have a socket library. 
* Wireshark: Application to show internet traffic on your machine
* telnet: Command line utility to connect to a socket/server using TCP. Can send whatever you like
* Postman: Application to easily send HTTP (and other) protocol requests 
* Flask: A http server library in python
