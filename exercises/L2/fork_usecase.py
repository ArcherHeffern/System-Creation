from os import fork

"""
Usecase: Performance improvements / Non blocking requests

IO Application which handles many requests from users
In order to handle all the applications in a timely manner, we will create a process for each request

Note1: Processes take computer resources to create, so don't do this all the time!

Note2: For now, all IO will be done through the Console (stdin, stdout, stderr)

Note3: There exist "Threads", which are like processes but take less resources. Their usage can lead to great performance improvements at at the expense of nondterministic and complicated code 
"""

def mail_server():
    while True:
        request: str = get_request()
        if fork() == 0:
            handle_request(request)


def get_request():
    return input()

def handle_request():
    """Do something with the request"""
    ...