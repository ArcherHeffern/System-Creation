Some clarifications: 
* Ports are implemented at the transport layer (TCP, UDP)
* Ports are used to differentiate applications, only one application to use a port at a time. Eg. Web servers run on ports 80 or 443

# Goal
Understand considerations of system design, system architectures, web development, and the protcols it relys on, HTTP and Websocket

## Designing systems: Considerations and Architecture styles
Similar to how we consider time and space complexity in COSI 12, we too have considerations when designing systems. There are reasons all of Amazons tech service aren't running on a single computer

*Performance, Scalability, Reliability, Modularity, Security, etc*

We break our applications into many parts (maybe run on different machines), use many architectures, and orchastrate interactions among these many parts to account for these considerations

*Our examples will revolve around file sharing: See image to explain*

Everything stems from client server, however, CDN and peer to peer are common enough that they can be thought of as their own 

### Client server
* One application provides a service (Server)
* One application uses the service (Client)
* Requires a protocol to facilitate communication
* Easy to implement
* Eg. Websites

Clarification: What is a server? 
* Server is the program we are running
* Think of it like a restaurant server. They wait for people to request food, and respond with the food. A servers job is to provide a service
    * Note that a server can also act as a client, restaurant servers in turn request food from the head chef, who in turn requests n chefs to start doing x y and z
* If we have a dedicated computer running the program, we could also call the machine a server 
* But at the end of the day, all we are working with, are programs

### CDN (Content Distribution Network)
* Don't worry about this
* Geographically distributed network of servers
* Reduces latency since servers are geographically closer to clients

### Peer to peer
* Also don't worry about it
* Everyone has same responsability, and does the same thing. 
* Eg. Bittorrent, Skype (Not anymore)

*At the end of the day, you can think of everything as client server with more abstractions*

### In depth Client Server
A computer can act as both a server and a client!

*Example: Classic web development model*
Client <-> Server <-> Database

Some less common but technically viable architectures  

Client <-> Database


       <-> Server
Client 
       <-> Database

*Practice: If we wanted to add payments to our service, and Stripe has a good payment service, how can we incorperate payments into our service?*

Examples of more complex architectures: GFS, Microservices, Micro-macroservices
* If you can imagine it, you can implement it

## Web Development
This is where we will start to specialize in web development

_Developer Perspective: Frontend and Backend_
* Backend is handling the cool computer logics, networking, managing servers, databases, etc
    * Frameworks make it easier to get started so you don't need to implement 500 page protocols from scratch
* Frontend is making the pretty html, css, and javascript files that the servers send in response to clients asking for them
    * Frameworks can make creating these pretty files easier 

_Runtime Perspective: Client Server_
* Client: Usually a web browser: Makes requests to Server(s) to get HTML, CSS, JS, and **data** those pages might need 
* Server: Serves web pages and data, orchastrates interactions between databases, and other servers providing services (eg. Payments with Stripe)

_At its most basic level_  
Just need a server that serves HTML documents using HTTP 

### HTTP: Hypertext Transfer Protocol
Protocol used by websites - Web browsers use HTTP automatically. 

* Client Server Design
* TCP on port 80

Q: Whats special about HTTP? Why don't we just use TCP?  
A: Its semantics relect common Database operations and getting files using file paths, also provides very web dev specific keywords (in headers), which are recognized and treated differently by web browsers


What does the agreement look like?

_Request (Client)_
VERB ROUTE HTTP-VERSION
HEADERS
BODY

VERBS 
* GET, PUT, POST, PATCH, DELETE (There are a few less known and less used verbs eg. OPTIONS, HEAD)
    * The main verbs reflect database operations...
    * CREATE, READ, UPDATE, DELETE
ROUTE 
* Think of a file path
HEADERS
* Key value pairs of metadata
BODY
* Text, the main payload

https://datatracker.ietf.org/doc/html/rfc2616#section-5

_Response (Response)_
HTTP-VERSION STATUS-CODE REASON-PHRASE
HEADERS 
BODY

STATUS-CODE
* Number ranging from 100 to 500, depending on how the request went. (Success, Client Issue, Server Failure, Redirect)
HEADERS
* Key value pairs of metadata
BODY
* Text, the main payload

There are many other features of HTTP we will learn later!

*Example with telnet: Get google home page: Show the actual request with wireshark*

In the future, we will use software to make these requests easier (Postman, thunder client)

In lower level protocols, the implementations almost always follow the specs to a T. HTTP not so much. This means you can technically do things not quite intended


## Recap
* Considerations for designing systems
* Basic architectures - Client server, CDN, peer to peer
* Advanced client server
* Web development overview
* HTTP

## Whats Next
Hands on: Creating a web server 

## Homework
Will be released friday

