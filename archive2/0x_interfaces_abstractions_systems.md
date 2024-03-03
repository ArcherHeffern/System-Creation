# What is programming about?
An academic will probably say



# Stuff
When starting out, I always had these concerns:  

1. Where does power come from?
2. What is the correct way to create a program?
3. How can I conceptualize the software world?

# Systems and Interfaces

Everything is interfaces

Interfaces have 2 main parts: The 4 basic operations, and the protocol
1. Open, Read, Write, and Close
2. How you use above operations

Examples: 


Operating System Layer: 
* IPC: Inter


# Interfaces and Power
We are going to Start by learning where we get power from. How we can create anything. You’re going to make some pretty unconventional scripts, just jamming tools together with some code, and that’s amazing. Becoming refined comes later.

API’s: They are the powerhouse of the world. No matter what, you will be using someone else’s technology, nobody sane is an actual purist in this profession (Try building an operating system and all the hardware from scratch! And then try getting all the tools and materials to do so by yourself as well! Oh yeah, and make sure to turn google off, that’s a tool as well!)

So the only reasonable way to do anything, is by using someone else’s code.

Software is a composition of building blocks - all connected together through interfaces. 

- SHOW THE IMAGE: Bottom to top and provide examples and whatnot - and then node.js module dependency chart - Software to software but also can go down or up the abstraction levels

— Explain API’s and whatnot

Now each time you want to use an API, you are going to have to learn it, search up its documentation, which is going to be tedious. Do I really have to know every single API?? Is there any direction?! 

Sort of. While software is a very complex place, with dependencies everywhere, like a hodgepodge of bricks making a semi functional wall, there are some softwares (and as such API’s) that are way more relevant, and some have such relevence that they be considered as paradigm shifters and treated as checkpoints. 

These checkpoint softwares are what we will learn, as well as some more specialized softwares. We will go up the abstraction levels from OS level to Distributed applications 

# TODO
Later we will discuss, not just API’s, but conventions / standards / Patterns that lead to paradigm shifters in the ways of distributed applications. Things such as the internet or web development directly arise from standards (found as RFC’s) or general preferences. 

############## 
Learning about API’s: the API’s themselves, and Protocols/Drivers (you might need to engage your communications in a specific manner (Usually there is already software you can use to facilitate this communication)
##############

# RANDOM NOTES: IGNORE
Start from low level=>Go to high level

The concept of an API is everywhere and there might be some misconception about what it means, as it applys to many things. 

API's are where true power comes from. While some may make your life easier by providing a service you didn't want to code up, others provide features that you could not possibly have access to otherwise. 

System calls  
Application that is running your program

Libraries/Code  

Any Interface for something Code related:
* can be a function header (is the interface for a function)


General ideas
* Where does our real power come from (API’s): Necessary tools
* Visualizing API’s as encapsulated Objects and how to string them together to create more interesting software. Building up through abstraction layers? 
* How can we not try to implement everything from scratch? (Note that every API, even the seemingly real power ones are merely just conveniences, right down the the bare metal. We are going to consider certain abstraction layers to be “checkpoints”, Due to how relevant they are and how much they shift the paradigm)
* Can you code
* Creating abstractions through indirection (conceptually every abstraction is just some sort of referencing/pointer)
    * Naming
    * Functions
    * Layers
    * Pointers

# API, Interface, Abstraction: An API Oritented Way to think about programming and the system that emerge
Interface Oriented Programming
Think of software as fully modular: Many modules all interacting with eachother through their interfaces: Its really a spiderweb
* The spiderweb can be thought of at many different levels of abstraction as well
    * Functions 
    * Modules (This is where you get the idea of )
    * Computers
    * IO


* API's that provide new functionality
* API's that make things easier

# 

The paradigm shifters:
* Hardware
* Operating System
* Distributed Applications: IPC and Computer Networking (IPC and Networking are all hardware or OS supported)

* Personal Code
* Business Code

Distributed applications: Libraries, Network, IO, Down to function calls


Visualizing software, getting an intuition for it: 
At base level: Functions, Input, Output -> You can string them together. Create a graph of connections
At single project module level: Many modules connected together
Introduce more advanced API’s: Many modules strung together connected through their IO. Either through


Common IO Patterns for stringing things together and how they can be used
File
* Persistant data
    * Database
* Config files

Command line
Network
IPC: Threading / multiprocessing
* Improved performance (Throughput, latency)


# On visualizing and Creating More Interesting software Projects