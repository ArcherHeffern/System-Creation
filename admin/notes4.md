Goal: 
You can conceptualize your systems and where power comes from
You can learn anything
You know what domain you are interested in 
You know the meta of your domain

Creating CLI's
Creating Network Programs
Using Frameworks/Libraries

==========================

What is programming:
// ?Input => Program => Output - Program can be conceptualized as many interfaces - in fact, input and output are also just interfaces

Interfaces
To create good code, you should know your environment, and that starts with the OS and hardware.

People who are more than casually interested in computers should have at least some idea of what the underlying hardware is like. Otherwise the programs they write will be pretty weird. - Donald Knuth

Go through all IPC's and system calls and then how they are used in order and how to create applications
1. Stdout
2. File: Databases and Git
3. Network
4. Frameworks, SDK's, and Libraries

// What about games IO like window and mouse / keyboard or microphone? How do we get access to peripheral hardware? 

Later: Get the more in depth intuition about systems and how they work - Just tell them how to hodgepodge shit together
===========================
_Interfaces_: Programming as wacky legos (Systems)
2 major parts: 4 basic commands, and protocol
Interfaces that provide power - Layers
Interfaces that make things easier : Drivers? - act to simplify the protocol layer - Frameworks, SDK's, Libraries, Transpilers, etc


You can think about product

There is no magic pill I can give you, you will need to code, and fail, and code again
How to code. Pretty simple. Just have an interest, and code. Use google to help you. 
_Productivity Tips_
* Iterative development 
* How to learn and research
* How to manage your project
* Common tools
* Common interfaces
* Where does power come from, how to jam things together



I am going to teach you all a model of thinking about software that can be applied to any domain. 

I find CS students at your level are very focused on technologies and languages, things that do not translate very well. 

Things like react, next, flask, javascript, jest, mongodb. 

This will be more conceptual and it may be difficult to start thinking in this way. 


1. What is programming about...

Solving Problems with: 
Algorithms
Data
and translating into code. 

These are the defecto standard of what programming is. However, this is very academic and does not translate very well into the real world. There are things missing.

Interfaces
Architecture, design, and _ patterns
tools (Tools you don’t use directly within your code)
 
What will I focus on 
Algorithms: No, these are highly domain specific and there are no algorithms that translate well. Instead, learn your domain, and read papers!

Data: No. You should already know most of the important ones (Arrays, Lists, HashMaps, Sets). And same as above, there are also specialized data structures in domains. 

Interfaces: This will the main focus of this education session. 

Architecture patterns: These are also specific to your domain, but we will learn about simple architectures for non-distributed and distributed systems (In that oder) later on. 

Tools: we will learn about the most relevant tools, such as git, __, and __. However, this will be done with a strong emphasis on being able to teach yourself

*Also, if you think of something interesting that works, don’t be afraid to implement it. New students are often too scared of doing this because they think there is a “Correct” way to do things*

Interfaces: 
Do all the drawing out



Patterns: 
Regular Applications under our interface model:

Distributed applications under our interface model: 

1 client application. Can Demarshall responses and listen for requests, can connect to any number of additional interfaces
1 main applications: Can Marshall and send requests
