import socket

"""
Server accepts an array of command and arguments as string - parses to an array - executes - and sends response back as string
"""

HOST = ''
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
server.bind((HOST, PORT))
server.listen(5)

conn, addr = server.accept()
with conn:
    print("Connected by", addr)
    while True: