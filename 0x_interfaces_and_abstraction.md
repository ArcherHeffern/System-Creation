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