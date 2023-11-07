Knowledge of the day: The anarchists cookbook

# Goal: Understand the fundamentals of the internet, and how everything builds off of it. 
This is a primer in system networking and system design. It will be more theoretical, pertaining to backend as a whole, and not just web development. 

We will start with the most bare bones components you can use, and then will build abstractions on top to provide certain functionality.
We will NOT delve into HOW data from point A to point B. I will provide resources for those of you who are interested in that. 

My goal is to not make you a web development engineer, but a software engineer.

## What is the Internet?
_3 Guiding principles_
* Best effort packet delivery service
* Power at the edge - end to end principle
    * A guideline for where to place functions in a layered system
    * Whenever possible, communications protocol operations should be defined to occur at the endpoints of a communications system
    * Keeps the network simple and scalable Allows for easy introduction of new services at the edges
* A network of networks

Q: For each of these, why?

## How is the Internet Organized?
Before we understand the organization, we should understand the idea of a protocol

### Protocols
A protocol is a system of rules that allows two or more entities of a communications system to transmit information via any variation of a physical quantity. 
The protocol defines the rules, syntax, semantics, and synchronization of communication and possible error recovery methods.

TLDR: It's just the agreement between 2+ parties how they are supposed to communicate (what syntax, what rules, etc)
TLLDR: Its a specification. It is up the programmer how exactly to implement it. 

_Example: The United States Mail System_
There is an agreement between all parties that you put a label with x format on the letter.
* If I gave a package with this label to an alien, they would have no clue what to do with it!
* If I give a package with this label to a USPS branch, they would know exactly what to do

_Practice: Electronic mail protocol_
Create a mail protocol

We have one computer acting as a person (Client)
We have one computer acting as a mail facility (Server)

Requirements: 
A user would like to be able to...
* Get their mail
* Send mail
* Create a mailbox
* Delete their mailbox
* Know who is also registered with the mailbox
*Don't worry about security*

What should the client send, what should the server expect, and what should the client expect to receive?

_Reading: [POP3](https://www.ibm.com/docs/en/i/7.5?topic=information-pop) (Post Office Protocol)_
Notes:
* This protocol is only for getting mail from a mail server, not sending! As such, you will not find any SEND commands
* It's a very simple protocol, that I would not recommend you to use.
* You can actually configure your Gmail to use POP3 (settings -> see all settings -> Forwarding and POP/IMAP)

Your homework for next meeting will be about TCP. A more advanced protocol that runs the world.

## Layering (TCP/IP Model)
Layering is a particular form of abstraction
The system is broken into a vertical stack of functions/protocols
The service provided by one layer is based solely on the service provided by layer below–This is the “up/down” interface

The internet is many *protocols* layered on top of eachother

4 sweeping layers of abstraction 
*Show diagram*

Link layer *lowest*
* Point to point communication - single hop
* For our purposes, we don’t care about this layer
Network layer
* Basic point to point communication - any # hops
* Uses link layer to accomplish
* No guarantees
End-to-end layer (Broken down into Transport and application layer) *highest*
* Provides specific guarantees depending on application (security, ordering, reliability, correctness, special syntax/semantics, etc)

_Example Mail_
*Draw out on whiteboard - walk through what each layer does and how affects the message being passed*
POP3: Mail protocol
TCP: Reliable connection
IP: Unreliable connection
Link layer...

*Show actual packets with wireshark*

## 3 Foundational Protocols: IP, TCP, and UDP
These 3 protocols run the world. Each of them provide different guarantees

### IP
The network layer gives the most basic functionality of the internet: Aka, the IP protocol
It runs the world and is what everything else is based on

If we visualize the layers and all the protocols, it's an hourglass
*Show image*

We use IP address to specify destination
Enables us to send “datagrams” from one computer to another

Interface: 
send(ipaddr, msg)

There are no guarantees about the datagrams reaching their destination
There are no guarantees the datagram reaches their destination correctly
No security, sends as plain text

Q: How does the end to end argument apply here? Why don’t we provide these guarantees at the IP layer?
A: How do we know the end user of IP actually needs those guarantees. eg. Phone calls

### TCP and UDP
These are built directly on top of IP, and also run the world, although at a slightly higher level of abstraction.

TCP is reliable, it is used for applications that need correctness
UDP is less reliable. Used by streaming 

## Sockets
Sockets: Putting things into action
Q: How can we use IP, TCP, and UDP? How can we go even lower? What is the lowest layer we are able to interact with and how?
A: Sockets

Sockets: Most basic way for you to access the network, is provided by your operating system. Allows you to send messages with TCP, UDP, and IP and access even lower abstractions with "raw sockets". Every major programming language should have a socket library. 
(You will most likely never use raw sockets)

Their API is designed to be similar to that of a file (open, read, write, close)

They also introduce an idea known as "ports", this is a way of breaking up all the traffic coming into your machine, into different sections, so different applications can choose what traffic to pay attention to by binding to a port

All of the networking tools you will use (flask, express, nginx, etc etc etc) EVERYTHING, uses sockets under the hood. 
#<Show flask using sockets>

_Example: Basic socket server in python_

## Takeaways
The internet is organized in layers
The importance of the end to end argument
Using IP, we can send messages from one computer to another
Sockets are the lowest level of abstraction we can directly use to send messages over the network

## Whats next 
Next lesson, we will design and implement our own end to end layer mail protocol

## Homework
Read the following article on TCP and answer the following questions. 

This is a case study into an advanced protocol called TCP. TCP provides guarantees such as reliable transport, correct ordering of packets, congestion control, and more! TCP is built on top of IP, an unreliable protocol which make a best effort attempt to get a packet from point a to b. When you are reading, think about how it achieves this and then answer the following questions. 

[General TCP](https://youtube.com/shorts/n-paFbO1hXE?si=vkHneFNQZLPygbS4)
[Reading](./static/reading.tcp.congestion.pnd_section6_3.pdf) for advanced question

1. Where in our model does TCP lie? What are some protcols built on top of it, and what is it built on? 
2. What does TCP do if a packet does not reach its destination. How does TCP know it was not recieved?
3. How does TCP guarantee correct ordering of packets?
4. How does TCP guarantee the data sent is the data recieved? 

(Optional) Advanced: How does TCP avoid "congestion collapse" (overloading the network by sending too much)? 

(Optional) Supplemental reading: [InternetWhitepaper](https://web.stanford.edu/class/msande91si/www-spr04/readings/week1/InternetWhitepaper.htm)

