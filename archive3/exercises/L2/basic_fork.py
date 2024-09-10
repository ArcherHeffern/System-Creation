#!/usr/bin/python3 

from os import fork

pid = fork()

if pid < 0:
    print("Error Forking")
elif (pid == 0): 
    print("This is child process")
else:
    print("This is parent process, the child process has id: %d" % pid)
