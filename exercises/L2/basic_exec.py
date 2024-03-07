#!/usr/bin/python3

from os import execve, environ

execve("/bin/ls", ["/bin/ls", "-la"], environ)