from os import read, write
import signal
from sock_util import *
import math
from dataclasses import dataclass

signal.signal(signal.SIGINT, lambda *x: exit(0))

NOT_ENOUGH_ARGUMENTS = "Not enough arguments: expected %s, found %s"
VALUE_ERROR = "Value Error: Expected string but got \"%s\""
UNKNOWN_COMMAND = "Unknown Command: %s" 
ERROR_STATUS = "ERROR"
SUCCESS_STATUS = "SUCCESS"

addr = "127.0.0.1"
port = 8080

@dataclass
class Error:
	error_message: str

	def __str__(self):
		return f"{ERROR_STATUS} {self.error_message}"

@dataclass
class Success:
	success_message: str

	def __str__(self):
		return f"{SUCCESS_STATUS} {self.success_message}"	

def log(msg: str):
	print(f"Server: {msg}")

def main():
	s = server_listen(addr, port, 5)
	if s is None:
		log("Null Connection")
		return
	print(f"Server: Listening to {addr}:{port}")
	while True:
		client = server_accept(s)
		tokens = client.recv(1024).decode().split()
		if len(tokens) == 0:
			continue
		command = tokens[0]
		match command:
			case "help":
				result = Success(__print_help())
				continue
			case "floor":
				result = __handle_floor(tokens)
			case "ceil":
				result = __handle_ceil(tokens)
			case "cos": 
				result = __handle_cos(tokens)
			case "sin":
				result = __handle_sin(tokens)
			case _:
				result = Error(UNKNOWN_COMMAND % command)
		client.sendall(str(result).encode())
		server_close(client)
	server_close(s)
	log("Shutting down server")

def __print_help() -> str:
    return  """
    floor <float>       : Floors a number
    ceil <float>        : Ceils a number
    cos <float>         : Cosine of a number
    sin <float>         : Sin of a number""" 

def __validate(tokens: list[str], num_tokens: int) -> Error|list[int]:
	size = len(tokens) - 1
	if size != num_tokens:
		return Error(NOT_ENOUGH_ARGUMENTS % (num_tokens, size))
	out = [0] * size
	try:
		for i in range(size):
			out[i] = float(tokens[i+1])
	except ValueError:
		return Error(VALUE_ERROR % tokens[i+1])
	return out

def __handle_floor(tokens) -> Error|Success:
    clean_tokens = __validate(tokens, 1)
    if type(clean_tokens) is Error:
        return clean_tokens
    return Success(str(math.floor(*clean_tokens)))

def __handle_ceil(tokens) -> Error|Success:
    clean_tokens = __validate(tokens, 1)
    if type(clean_tokens) == Error:
        return clean_tokens
    return Success(str(math.ceil(*clean_tokens)))

def __handle_cos(tokens) -> Error|Success:
    clean_tokens = __validate(tokens, 1)
    if type(clean_tokens) == Error:
        return clean_tokens
    return Success(str(math.cos(*clean_tokens)))

def __handle_sin(tokens) -> Error|Success:
    clean_tokens = __validate(tokens, 1)
    if type(clean_tokens) == Error:
        return clean_tokens
    return Success(str(math.sin(*clean_tokens)))

if __name__ == '__main__':
	main()
