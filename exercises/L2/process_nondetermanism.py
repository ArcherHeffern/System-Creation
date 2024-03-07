#!/usr/bin/python3

from os import fork, wait

for size in [100, 1000, 10000, 100000]:
    print(f"Size: {size}")
    pid = fork()
    if pid == 0:
        print("Child")
        exit(0)
    else:
        for _ in range(size):
            ...
        print("Parent")

        wait()
        print()