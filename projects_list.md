# Projects List
## Internet-Less Applications: Mobile, Desktop, Terminal 
### Getting Started
Pick a language, figure out what IO and API's are avaliable in your environment and just code. Pretty much think of any application with a UI (Terminal, GUI, etc) do some research and implement it.  

I would highly recommend...
* creating a todo list app in the terminal which doesn't save between executions of the program
* then give it a UI
* then make data persist between executions by saving to files

### Projects
* See the Embedded Section
* See the Interpreters / Compilers Section
* See the Data Science / Machine Learning Section
* See the Concurrency Section
* TODO List
* Scheduling App
* [Hackathon project](https://mlh.io/seasons/2024/events): Look at the prompts and just make something. Bonus if you win
* Compression Tool (think zip or gzip) using Huffman encoding
* JSON parser
* update_alternatives clone
* regex evaluator using finite state machines
* search engine (start using TF-IDF)
* 6502 microprocessor emulator 
* Command line procedurally generated game (Eg. Elite; 1984)
* Database recovery mechanism
* Discord Bot
* Chess Bot
* Chess board manipulation library
* Portfolio analysis tool

## Distributed (Internet Using) Applications
Nearly of the applications above can be made into Internet Applications. Exception for environments that do not offer networking capibilities (Probably the discord bot). 

The internet opens up a world of possibilities when it comes to applications. At its most basic level it allows data to flow between computer across the world. Some new properties are...

1. providing services instead of having users download software, this is good for...
    * Subscription based services
    * Hiding our implementation details (IP)
    * Improving performance for user (They don't need a good computer)
    * Improving convenience for user (They don't have to install an entire application to use it just once)
2. Global Multi User Applications
    * Chat / VoIP
    * World Wide Web
    * Gaming

### Getting Started
Knowing how to make basic applications is a prereq for this section. Create the TODO list app from the "internet-less application" section. Then make the following improvements:
* make it accessable over network using sockets (remove the existing UI), just have it send strings over the network, test with `netcat`
* upgrade so instead of sending raw strings, send strings in HTTP format, you should now be able to test with a web browser
    * This is kinda painful so you may want to bring in a framework: (Python: Flask, Java: Spring, Javascript: Express, C: haha)
* improve the UI by having socket send HTML 
* improve the data persistence by using a heavy database (Either a SQL DB or MongoDB) - You will probably want to use a library to interface with the database (Or you could do it from scratch but that won't be fun)  

Then do the getting started section for "Computer Networking" (Or do it first)

### Projects
* See the Computer Networking Section
* See the Distributed System Section
* __personal website__: Link on your github / LinkedIn
* Create a REST or GraphQL API that provides data on X
* Trading Bot

## Specialized Applications
### Embedded / IOT / Engineering
#### Getting Started
Get an Arduino or raspberry PI, check out cool things engineers make and make something. Find engineers or an engineering lab on campus so you don't have to pay as much to get started. They may even lend you an Arduino. 

#### Projects
* Beverage robot
* Smart couch
* Smart home automation
* Battle bot
* [Party Button!](https://youtu.be/R_kYaPZ6eds?si=1K69JwoB3ir_fC97)

## Compilers / Interpreters
### Getting Started
This book is amazing: [Crafting Interpreters](https://craftinginterpreters.com/)  

You follow these later for a more academic approach:  
[Compilers: Principles, Techniques, and Tools](https://en.wikipedia.org/wiki/Compilers:_Principles,_Techniques,_and_Tools)  
[Principles of Compiler Design](https://en.wikipedia.org/wiki/Principles_of_Compiler_Design)  

### Projects
* Create a lisp interpreter
* Assembly interpreter
* Math expression interpreter
* [Dreamberd](https://github.com/TodePond/DreamBerd---e-acc)
* Design and implement a language
* Create tooling for your language (LSP Support, Formatter, Linter, Debugger, Documentation)

## Computer Networking
### Getting Started
Read this [Internet whitepaper](https://web.stanford.edu/class/msande91si/www-spr04/readings/week1/InternetWhitepaper.htm) for broad picture.
Use sockets to implement a basic TCP web proxy that supports 1 connection, use [netcat](https://en.wikipedia.org/wiki/Netcat) to test. 
* Follow [this](https://www.scs.stanford.edu/07wi-cs244b/refs/net2.pdf) guide on using sockets. I'd suggest if you have time learning C in the process, its a suprisingly simple and elegant language, and will help you understand so much more. (Or don't and use sockets in your preferred language). Sockets are the lowest level abstraction you (reasonably) have access to, provided directly by the operating system through system calls. 
* Once you are done, there are several improvements you can make:
    * Increase number of users
    * Improve performance by using threading (pthreads) or async IO (described in the guide)
        * Implement event driven architecture
    * Ensure no buffer overflows are possible

For more comprehensive networking knowledge, [this](https://en.wikipedia.org/wiki/TCP/IP_Illustrated) book is a classic  
For exact details of how internet architecture should be implemented, see the RFC's  
* eg. [Requirements for IPV4 Routers](https://datatracker.ietf.org/doc/html/rfc1812)

### Projects
* HTTP server from scratch (using sockets and string processing, see the HTTP RFC for reference)
* Internet Relay Chat (IRC) Client
* URL Shortener
* SOCKS proxy
* DNS Resolver
* VPN Client
* Redis Server
* NAT hole puncher
* Map Reduce clone
* Google file system clone

### Projects Which Are Typically Used in Networking Applications but Don't Directly Need to Have Sockets or Network Included
* Rate Limiter
* Message broker
* Application load balancer

## Concurrency
### Getting started
Understand general operating systems concepts, then work through the following 5 items in their order

* Low Level: Build Locks (Test and Set or other) (lock, unlock, trylock)
* thread Level: Build a small threads package
* Custom user threads library (many to 1, 1:1, many to many)
* Synchronization Level: Build mutexes and semaphores
* Application Level: Producer and consumer (… type problems)

### Projects
* The above are also projects
* Multiple editing of 1 doc
* Implement a thread pool
* Concurrent web scraper: Scrape data from devpost and compile into CSV

## Distributed Systems
### Getting Started
This quite a hard dicipline, and I don't know too much about it. You can consider this extreme networking. This field its at the intersection of industry and acadamia so reaching out to a professor is your best bet (for 'Desians see Professor Luiba). 

### Projects
* [these](https://fly.io/dist-sys/) challenges 
* Skype clone using original Peer to peer architecture
* 2 Phase commit
* Distributed Hash Table

## Data Science / Machine Learning
### Getting Started
* Complete some Kaggle courses, learn a data analysis language (Python, Julia, R, Matlab), learn of the libraries avaliable, then...
* Compete in [Kaggle](https://www.kaggle.com/) 
* Join [hackathons](https://mlh.io)
* Do research, reach out to professors or a lab
