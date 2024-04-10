from os import read, write
from sys import stderr
from sock_util import *
from math_server import NOT_ENOUGH_ARGUMENTS, UNKNOWN_COMMAND, VALUE_ERROR, ERROR_STATUS, SUCCESS_STATUS

"""
This is convenient because we don't need to have to know the network protocol and it handles all the connection and IPC logic for us. This is especially important for more complex protocols 

While I did not do this, connect, floor, ceil, etc, would also make sense as functions which will take a connection struct as an argument. This is up to you. 

"""

def log(msg: str):
	print(f"Client: {msg}", file=stderr)

class RemoteMathLib:
	def __init__(self, host: str = "127.0.0.1", port: int = 8080):
		self.host = host
		self.port = port

	def __handle__(self, command: str, *values) -> int:
		msg = command + " "
		for value in values:
			msg += str(value) + " "
		s = server_connect(self.host, self.port)
		if s is None:
			log("Connection Error")
			exit(1)
		s.sendall(msg.encode())
		result = s.recv(1024).decode()
		server_close(s)

		tokens = result.split(maxsplit=1)
		status = tokens[0]
		if status == SUCCESS_STATUS:
			return float(tokens[1])
		else:
			log(tokens[1])
			return None
        

	def floor(self, x: int) -> int|None:
		return self.__handle__("floor", x)

	def ceil(self, x: int) -> int|None:
		return self.__handle__("ceil", x)

	def cos(self, x: int) -> float|None:
		return self.__handle__("cos", x)

	def sin(self, x: int) -> float|None:
		return self.__handle__("sin", x)
