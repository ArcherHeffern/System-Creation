# Applications 
## Why
Software development is a large place, there is so much to do. However, applications are very relevent in todays day and age.  
Q: Why applications, why aren't we doing web development or mobile app?  
A: They are all so similar, to specialize now would be a crime to you all  

## Examples
There are many types of business applications
1. Terminal Based
2. Websites
3. Mobile
4. Desktop

While seemingly very different...

Differences: 
* Installation
* Languages
* APIs

They are very similar and arise from the same roots 
2 Components
* IO
* Functionality

<!-- TODO: Expand on this -->
Our approach: 
start with just a basic terminal program with a basic UI - non stateful, we run the program once and we do commands from inside. Then we make it run one command at a time and stores data in files. We can now start thinking about making our UI Better... we can also start thinking about making storing more complex data easier and more reliable with a database

__IO Options__
* GUI (Java Swing, OpenGL, Tkinter, etc)
* Write to files (system calls: open, read, write, lseek, close)
* Network (sockets) -> Send data to any other sockets on your network (system calls: socket, bind, accept, listen, connect)
* Speaker / other peripheral IO Devices
* Other [IPC](https://en.wikipedia.org/wiki/Inter-process_communication) methods

Some of these are good for UI, some, not so much

Real world examples: 
* GUI: Desktop applications
* Files: Filetype conversion tools
* Network: Yeller Program - recieves messages from user through network (eg. address 127.0.0.1 port 8080) and sends back message uppercased
* Speaker: Zoom

These IO Options aren't just for to interface with the user. We can use them to perform "other" roles.  
*Note: Multiple IO devices are frequently used in a single program*

Q: Brainstorm how we can use Files and the network for actions other than directly interfacing with the user
A: 
* Files are good for storing data between executions of a program
* The network is good for communicating with other programs (globally), making your program accessable (globally), and generally sending information to a machine anywhere on earth assuming internet connection
    * Note: A computer can send network requests to itself


# Practice
1. Mail program. Only accessable from the machine its on and when the program ends all information is lost. Interaction happens at the command line
2. ... Now data should persist
3. ... Now create a nice user interface for it. <!-- TODO: The ordering here seems wrong - also whats up with mobile app ;-; eugh explaining server and application is going to be a pain here TODO: figure this out-->
4. ... This is where the methods differ: Make it globally accessable. If website or app create backend 

Note to self: Network can be easily reasoned about by thinking of it as; instead of sending commands through the command line, we are now sending the exact same commands through the network. show image of this later