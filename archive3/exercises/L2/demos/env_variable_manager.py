#!/usr/bin/python3
from os import environ, path
from sys import argv

ERR_NOT_ENOUGH_ARGS = 1

def print_usage():
    basename = path.basename(argv[0])
    print("Usage: ")
    print(f"{basename} get <variable>")
    print(f"{basename} set <variable> <value>")

if len(argv) < 3:
    print_usage()
    exit(ERR_NOT_ENOUGH_ARGS)

command = argv[1]
variable = argv[2]

if command == "get":
    print(environ.get(variable))
elif command == "set" and len(argv) == 4:
    value = argv[3]
    environ[variable] = value
else:
    print_usage()

# Test getting: PATH, SHELL, HOME

# Question: 
# Why if we set environ and then get it, the change does not show up? 