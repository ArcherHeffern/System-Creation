from flask import Flask, request
import sqlite3
sqlite3.connect('hello')

app = Flask(__name__)

mail = {}

transaction
I pay you 200 dollars
sub from me
adds to you

# GET /person/archer

@app.get('/person/<name>?') # return  hello world
def root(name):
    method = request.method  # This is going to be get
    url = request.url
    return f'You made a request to {url} with method {method}'

# Create your own route that returns "Hi mom"


app.run('0.0.0.0', 8080)


# Route parameters




# Query string parameters


# Mail server Requirements:
"""
_Send Mail_
* Send message
* Get message
* Create mailbox
* Delete mailbox

* Edit message
* Delete messages

Request: 
POST /message
Content-Type: application/json

{
from: <from>,
to: <to>,
message: <message>
}

Response:
200 OK

400 BAD REQUEST 

mailbox does not exist
empty message

TODO: Get mail
"""
