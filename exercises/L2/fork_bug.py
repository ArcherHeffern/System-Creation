#!/usr/bin/python3
from os import fork

"""
Expected output: 
"Hello from child!" and "Hello from parent!" printed 10 times each
"""

for i in range(10):
    if fork() == 0:
        print("Hello from child!")
    else:
        print("Hello from parent!")