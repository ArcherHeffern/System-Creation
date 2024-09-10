#!/usr/bin/env python3

# These are special functions! They are system calls!	
from os import fork, wait, execvp, chdir

while True:
    commands: list[str] = input("> ").strip().split()
    if len(commands) == 0:
        continue
    
    command: str = commands[0]

    # Process any builtins
	match command:
		case 'exit':
			exit(0)
		case 'cd':
			if len(commands) == 2:
				chdir(commands[1])
			continue

    # If no builtins, execute command in a new process
    if fork() == 0:
        try:
            execvp(command, commands)
        except:
            print("Invalid command [%s]" % command)
            exit(1)
    wait()
