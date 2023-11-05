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

## Designing systems: Architecture styles
How do we design our applications? #TODO: Reword
Considerations: Complexity vs Scalability

*Explain scalability*

*Our examples will revolve around file sharing: See image to explain*

### Client server
* One machine provides a service
* Easy to implement
* Eg. Websites

Clarification: What is a server? 
* Server is the program we are running
* If we have a dedicated computer running the program, we could also call the machine a server 
* But at the end of the day, all we are working with, are programs

### CDN (Content Distribution Network)
* Geographically distributed network of servers

### Peer to peer
* Also don't worry about it
* Eg. Bittorrent, Skype (Not anymore)

How is this layering done programattically?

## In depth Client Server
A computer can act as both a server and a client!

*Example: Classic web development model*
Client <-> Server <-> Database

*Practice: TODO: Add payments? *
* Even more complicated with GFS (Google file system)* 

# Web Development
This is where we will start to specialize in web development
Frontend and backend
* Backend is handling the cool computer logics, networking, managing servers, databases, etc
* Frontend is making the pretty html, css, and javascript files that the servers send in response to clients asking for them

TODO: Something about javascript and URLs being the bridge between the two. 

## HTTP
Protocol used by websites - Web browsers use HTTP automatically. 

Is used with client server architecture, which is reflected in the protocol

HTTP uses TCP
Q: What does this say about HTTP?
A: HTTP is a very reliable application layer protocol

What does the agreement look like?

_Request (Client)_
VERB ROUTE HTTP-VERSION
HEADERS
BODY

https://datatracker.ietf.org/doc/html/rfc2616#section-5

_Response (Response)_
HTTP-VERSION STATUS-CODE REASON-PHRASE
HEADERS 
BODY

There are many other features of HTTP we will learn later!

*Example with telnet: Get google home page: Show the actual request with wireshark*

In the future, we will use software to make these requests easier (Postman, thunder client)

*Practice: TODO*


## Tech Recap
* Sockets: Most basic way for you to access the network, is provided by your operating system. Allows you to send TCP, UDP, and IP messages and access lower abstractions with "raw sockets". Every major programming language should have a socket library. 
* Wireshark: Application to show internet traffic on your machine
* telnet: Command line utility to connect to a socket/server using TCP. Can send whatever you like
* Postman: Application to easily send HTTP (and other) protocol requests 
* Flask: A http server library in python
