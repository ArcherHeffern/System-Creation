#!/usr/bin/python3

from os import wait, fork 
from time import sleep

pid = fork()

if pid == 0:
    print("Child process runs to completion...")
    for i in range(1, 6):
        sleep(.5)
        print(f"\r{i}", end="")
    print()
else:
    wait()
    print("And then the parent runs...")