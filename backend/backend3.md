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

How is this layering done programatically?

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
1. client sends request
2. server rends response

You may notice this is nothing new. So whats special about HTTP? 
Its semantics relect  - REWORD - Database and getting files using file paths

HTTP uses TCP
Q: What does this say about HTTP?
A: HTTP is a very reliable application layer protocol

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

*Example with custom 

In lower level protocols, the implementations almost always follow the specs to a T. HTTP not so much. 

HTTP web server implementations fall into 2 categories, "Batteries included", and "Batteries not included". 

Batteries included provide a lot for you.

Batteries not included provide more freedom at the expense of needing to write more and perhaps being "technically" not correct. 

## Recap

## Whats Next

## Homework

1. Databases

2. 
