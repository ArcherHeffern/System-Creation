[Roadmap](https://youtu.be/66tfvFeALBQ?si=l_BVcDWDUTRSM_u6) for Web Dev, Desktop, Mobile, Hardware, Game Dev, ML, and Low level systems

# Projects List

## Applications: Web Dev, Mobile, Desktop, Terminal Based 
### Getting started
See the above video. This grouping may seem quite strange, but the actual projects you can do for each of these overlap a lot. A TODO list with a proper backend and database is the best starter project. You should also make a personal website, host it, and link it on github and LinkedIn.

- They all are applications - they provide a service to end users
- They all have a concept of frontend and backend - All it depends on is if half the application is split over the network
- They all can have very similar arcitectures (Frontend, Backend, API's, Database), even if you may see this less often in termial applications

### Projects
* __personal website__: Link on your github / LinkedIn
* TODO List
* [Hackathon project](https://mlh.io/seasons/2024/events): Look at the prompts and just make something. Bonus if you win
* Scheduling App
* Think of any application with a UI

## Embedded / IOT / Engineering
### Getting Started
Get an Arduino or raspberry PI, check out cool things engineers make and make something. Find engineers or an engineering lab on campus so you don't have to pay as much to get started. They may even lend you an Arduino. 

### Projects
* Beverage robot
* Smart couch
* Smart home automation
* Battle bot
* [Party Button!](https://youtu.be/R_kYaPZ6eds?si=1K69JwoB3ir_fC97)

## Compilers / Interpreters
### Getting Started
These books are amazing  
[Crafting Interpreters](https://craftinginterpreters.com/)  
[Compilers: Principles, Techniques, and Tools](https://en.wikipedia.org/wiki/Compilers:_Principles,_Techniques,_and_Tools)  
[Principles of Compiler Design](https://en.wikipedia.org/wiki/Principles_of_Compiler_Design)  

### Projects
* Create a lisp interpreter
* Assembly interpreter
* [Dreamberd](https://github.com/TodePond/DreamBerd---e-acc)
* Design and implement a language

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
* SOCKS proxy
* DNS Resolver
* VPN Client
* Redis Server
* NAT hole puncher
* Map Reduce clone
* Google file system clone

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
* Complete the Kaggle courses, compete in [Kaggle](https://www.kaggle.com/) 
* Join [hackathons](https://mlh.io)
* Do research, reach out to professors or a lab

## Misc
* __[Hackathon project](https://mlh.io/seasons/2024/events)__
* URL Shortener
* Application load balancer
* Rate Limiter
* Message broker
* Compression Tool (think zip or gzip) using Huffman encoding
* JSON parser
* update_alternatives clone
* regex evaluator using finite state machines
* search engine (start using TF-IDF)
* 6502 microprocessor emulator 
* Command line procedurally generated game (Eg. Elite; 1984)
* Database recovery mechanism
* Create a REST or GraphQL API that provides data on X
* Trading Bot
* Discord Bot
* Chess Bot
* Chess board manipulation library
* Portfolio analysis tool

<!-- Potential Sections -->
## Command Line Tools
## Non End User Facing Services / Things???
* API
* SDK
* Libraries