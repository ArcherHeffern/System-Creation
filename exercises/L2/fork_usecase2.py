#!/usr/bin/python3

from time import sleep
from random import randint
from sys import argv
from os import fork, wait
from pathlib import Path

# Parallel processing Example
# For performance improvements
# Processes many files using 1 process per file 

EXT_ERR_NOT_ENOUGH_ARGS = 1

def main():
    # Argument parsing
    if '-w' in argv:
        start = 2
        _wait = True
    else:
        start = 1
        _wait = False
    if len(argv) <= start:
        print("Usage: fork_usecase2.py [-w] files ...")
        exit(EXT_ERR_NOT_ENOUGH_ARGS)

    # Parallel processing
    for i in range(start, len(argv)):
        filename = argv[i]
        if Path(filename).is_file() and fork() == 0:
            process_file(filename)
            exit(0)
    
    # To wait or not to wait, that is the question...
    if _wait:
        wait()
        print("Completed processing")


def process_file(filename):
    """Imagine this is a long running task"""
    sleep(randint(1, 5))
    print(f"{filename} finished processing")
    

if __name__ == "__main__":
    main()