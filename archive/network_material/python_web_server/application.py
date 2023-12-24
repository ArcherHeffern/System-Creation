from flask import Flask, request

app = Flask(__name__)


@app.get('/')
def root():
    method = request.method  # This is going to be get
    url = request.url
    return f'You make a request to url {url} with method {method} ', 200


app.run('0.0.0.0', 8080)
