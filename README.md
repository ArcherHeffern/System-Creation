# Preface
I wrote this education for the purpose of helping students gain enough understanding and intuition of Software that they could do anything they wanted. While the end will focus a bit more on Web Development, it is done in such a way that it enhances the lessons I want to teach. 

People think that computer science is the art of geniuses but the actual reality is the opposite, just many people doing things that build on each other, like a wall of mini stones.  - Donald Knuth

The development of software is also the same. No matter what you are going to be using someone else software, or hardware and its going to be messy. Thats not to say there aren't checkpoints where there is an invention so pivotal and so foundational that we can just learn the one thing and build from there. 

We are going to learn in depth the foundational API's. Starting from the OS level, working our way up building applications and later distributed applications with them, and then delving into the world of networking and even more complicated distributed applications that come with it.

Core things when doing a project:
* Know the language
* Know the avaliable Interfaces
    * OS Syscalls
    * User Interfaces
    * IO
    * API's
    * Application running on (Recursive)
* Know your dev tools 
    * Managerial (git, debugger, code editor, notes app, Command line - TLDR: Helper applications that don’t themselves don’t spit out code)
        * Helper Applications and thing to install said applications
    * Code gen (Package manger (For programming language), libraries, SDK?)

* Being a good programmer
    * System Design
    * Good code
    * Debugging
    * Research capabilities

# Tamid Education Ideas


Review standard library? 
- OS and SYS modules

Other type of program IO: Used by other programs 
- Libraries
- Config files



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