#!/usr/bin/python3
from os import fork

for i in range(10):
    if fork() == 0:
        print("Hello from child!")
    else:
        print("Hello from parent!")