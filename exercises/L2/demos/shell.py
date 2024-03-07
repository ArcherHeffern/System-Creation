#!/usr/bin/python3

from os import fork, wait, execvp

while True:
    commands = input("> ").strip().split()
    if len(commands) == 0:
        continue
    
    command = commands[0]

    if command == 'exit':
        exit(0)

    if fork() == 0:
        execvp(command, commands)
    wait()