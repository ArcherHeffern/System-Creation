#!/usr/bin/python3

from os import execve, fork, wait, environ

pid = fork()

if pid == 0:
    execve("/bin/ls", ["/bin/ls"], environ)
    print("This will never execute")
elif pid > 0: # Parent process
    wait()
    print("Completed")
else:
    print("Error Forking")