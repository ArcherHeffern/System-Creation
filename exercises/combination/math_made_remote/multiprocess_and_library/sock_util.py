from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
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
        s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen(backlog)
    except Exception as e:
        print(f"Exception: {str(e)}", file=stderr)
        return None
    return s

def server_close(s: socket):
	s.close()

def server_accept(s: socket) -> socket:
    """Accept incoming connection from listening server"""
    return s.accept()[0]

def server_connect(host: str, port: int) -> socket:
    """Connect to remote server"""
    s = socket(AF_INET, SOCK_STREAM, 0)
    s.connect((host, port))
    return s
