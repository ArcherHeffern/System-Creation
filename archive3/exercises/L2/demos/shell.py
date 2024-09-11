#!/usr/bin/env python3

# These are special functions! They are system calls!	
from os import fork, wait, execvp, chdir

RUN_PROGRAM = execvp
CREATE_NEW_PROCESS = fork
WAIT_FOR_RUNNING_PROGRAM_TO_FINISH = wait
CHANGE_DIRECTORY = chdir


while True:
    tokens: list[str] = input("> ").strip().split()
    if len(tokens) == 0:
        continue
    
    command: str = tokens[0]
    args = tokens

    # Process any builtins
    match command:
        case 'exit':
            exit(0)
        case 'cd':
            if len(args) == 2:
                CHANGE_DIRECTORY(args[1])
            continue

    # If no builtins, execute command in a new process
    if CREATE_NEW_PROCESS() == 0:
        try:
            RUN_PROGRAM(command, args)
        except:
            print("Invalid command [%s]" % command)
            exit(1)
    WAIT_FOR_RUNNING_PROGRAM_TO_FINISH()
