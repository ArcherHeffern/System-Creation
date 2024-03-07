from os import fork

pid = fork()

if (pid == 0): # In child process
    print("This is child process")
else: # In parent process
    print("This is parent process")
