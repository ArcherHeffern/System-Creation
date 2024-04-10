from socket import socket, AF_INET, SOCK_STREAM
from sys import stderr

__all__ = [
    "server_listen",
    "server_close",
    "server_accept",
    "server_connect"
]

def server_listen(host: str, port: int, backlog: int) -> socket|None:
    """Create server"""
    try:
        s = socket(AF_INET, SOCK_STREAM, 0)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen(backlog)
    except Exception as e:
        print(e, file=stderr)
        return None
    return s

def server_close(s: socket):
    s.close(s)

def server_accept(s: socket) -> socket:
    """Accept incoming connection from listening server"""
    return s.accept()[0]

def server_connect(host: str, port: int) -> socket:
    """Connect to remote server"""
    s = socket(AF_INET, SOCK_STREAM, 0)
    s.connect((host, port))
    return s