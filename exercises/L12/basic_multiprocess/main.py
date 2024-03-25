from os import fork, pipe
from math_server import handle as handle_remote
from math_client import handle as handle_client

remote_read, local_write = pipe()
local_read, remote_write = pipe()

if fork() == 0:
    handle_remote(remote_read, remote_write)
else:
    handle_client(local_read, local_write)