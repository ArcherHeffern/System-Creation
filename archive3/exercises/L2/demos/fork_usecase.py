#!/usr/bin/python3

from os import fork
from random import randint
from time import sleep

"""
Usecase: Performance improvements / Non blocking requests
How: When recieving a request, spawn a process to handle and continue reading input in main process
"""

def mail_server():
    while True:
        request: str = input("> ")
        if request in ['q', 'quit', 'exit']:
            break
        if fork() == 0:
            handle_request(request)
            exit(0)


def handle_request(request: str) -> int:
    """Do something with the request"""
    sleep(randint(1, 5))
    print("Handled request [%s]" % request)


mail_server()