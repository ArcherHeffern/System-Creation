#!/usr/bin/python3
from os import execvp

execvp("./process_components.py", ["./process_components.py", "Hello", "world"])