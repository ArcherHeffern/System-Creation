#!/usr/bin/python3

from os import fork 

pid = fork()

if pid == 0:
    process = "Child"
else:
    process = "Parent"

for i in range(1_000_000):
    print(process)