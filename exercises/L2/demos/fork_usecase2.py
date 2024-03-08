#!/usr/bin/python3

from time import sleep
from random import randint
from os import fork
from pathlib import Path

# Parallel processing Example
# For performance improvements
# Processes many files using 1 process per file 
# See the follow up to this in compression.py

FILES = ["a.txt", "b.txt", "c.txt"]

def main():
    for file in FILES:
        if Path(file).is_file() and fork() == 0:
            process_file(file)
            exit(0)
    

def process_file(filename):
    """Imagine this is a long running task"""
    sleep(randint(1, 5))
    print(f"{filename} finished processing")
    

if __name__ == "__main__":
    main()