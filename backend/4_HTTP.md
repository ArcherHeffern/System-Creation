# Review: 
* Client server architecture
* HTTP
    * Application layer protocol built on TCP using port 80
    * View img of how HTTP req/res messages are formatted
    * Remember! All HTTP messages are just specifically formatted strings!
    * Remember! HTTP is on application layer, so the actual internet message looks more like...

# Goal: Hands On - Create a Mail Web Server
In the process, we will learn how to send web pages (HTML, CSS, JS) and supplementary data the websites may request (JSON, raw strings, csv, etc)  

We will also go over some other features HTTP provides that will prove to be useful

Language doesn't matter too much, so we will be doing this in both java and python!

* To test your server, use netcat on the command line
```bash
nc <url> <port>
GET /
```

# General Model for Web Server Librarys
// function called when METHOD and URL match
@get('/name')
function Route(request as object)
    name = request.body

    ...Do logic stuff...
    response = new Response()
    response.status = 200
    response.headers.content-type = "application/json"
    response.body = "<div>Hello ${name}<div>"

    return response 

Web servers librarys are just TCP socket servers that...
* parse the incoming messages into a nice object according to HTTP
* call the correct function according the the request line
* allow you to create a response and do whatever you want
* will send the response as a properly formatted http message over the socket

*They make it so you don't have to work with raw strings and constantly reference the HTTP RFC documentation about all the nuances*

# Hello world Server
Choose either python or java to code in.  

Create a HTTP web server with 2 endpoints, one at "GET /", which returns "hello world", and another that returns "hi mom"

* If you finish early, change one to return a HTML anchor tag, referencing the other page. 
*What do you think is happening under the hood when a user clicks on the anchor tag?*

## Some additional HTTP Features
1. Route parameters
Routes can have variable parts
eg. /user/age  
Age can be the variable, so when the client navigates to /user/19, the 19 is parsed out

2. Query string parameters
We can put key value pairs at the end of a route
eg. /usr?age=19

# Basic Mail Web Server
Lets come up with a a game plan...
1. What functionality do we provide?
2. What are our endpoints? (Same idea as when we created a mail protocol, just this time is with HTTP!)

* Don't worry about authentication, lets assume everyone is an upstanding citizen

_Ways to update your page_
1. Self updating HTML pages
    * Javascript heavy (used to send custom HTTP requests, parse responses, and update UI)
    * HTTP data responses are easy to parse text data called hypermedia (eg. CSV, JSON)
2. Get new page
    * Just use hyperlinks and send HTML

# Takeaways
* Hypermedia formats: CSV, JSON, etc

# Whats next
* Adding state with a database

# Homework
* Finish up the mail server
Challenges:
* Add authentication - theory: User gives a password. We store the password. User must provide password for every action. In the real world, the server will give back a random(ish) string, for the client to authenticate with. That way permissions can easily be revoked and so passwords aren't easily accessable. 
* Add persistance without a database (write to a file), parse it on application startup to recreate data structures

Super Challenge:
* Create or think of how you would create your own HTTP server/framework/library using sockets (This would look awesome on your github/resume!)
