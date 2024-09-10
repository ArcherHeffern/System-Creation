import socket
from os import system
from sys import stderr
from typing import NewType

"""
Remote procedure call pattern
"""

NOT_ENOUGH_ARGS = "Not enough arguments, expected %d"

HOST = '127.0.0.1'		# The Host of the server
PORT = 8080				# The same port as used by the server

def main():
	while 1:
		print("> ", end="")
		tokens = input().split()
		if len(tokens) == 0:
			continue
		command = tokens[0]

		match command:
			case "exit"|"q"|".exit":
				break
			case "clear":
				system("clear")
			case ".help":
				print_help()
			case "login":
				login(tokens)
			case "logout":
				logout(tokens)
			case "list_users":
				list_users(tokens)
			case default:
				status, msg = send(" ".join(tokens))
				if not status:
					print(msg, file=stderr)
				else:
					print(msg)
	print("Exiting...")

def print_help():
	print("TODO")

def list_users(tokens):
	if len(tokens) < 2:
		print(NOT_ENOUGH_ARGS % 2)
		return
	res, msg = send(f"list_users {auth_token}")
	if not status:
		print(msg, file=stderr)
	else:
		users: list[str] = msg.split()
		print("Users: ")
		for user in users:
			print(user)


def login(tokens):
	if len(tokens) < 3:
		print(NOT_ENOUGH_ARGS % 3)
		return
	username = tokens[1]
	password = tokens[2]
	status, msg = send(f'login {username} {password}')
	if not status:
		print(msg, file=stderr)
	else:
		print(f'Token = {msg}')


def logout(tokens):
	"""Invalidates the token"""
	if len(tokens) < 3:
		print(NOT_ENOUGH_ARGS % 3)
		return 
	username = tokens[1]
	token = tokens[2]
	status, msg = send(f'logout {username} {token}')
	if not status:
		print(msg, file=stderr)
	else:
		print(msg)
	
Status = NewType('Status', bool)
Msg = NewType('Msg', str)
Response = NewType('Response', tuple[Status, Msg])

def send(request: str) -> Response:
	try:
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			s.connect((HOST, PORT))
			s.sendall(request.encode())
			res_tokens = s.recv(1024).decode().split(maxsplit=1)
			str_status = res_tokens[0]
			if str_status == "0":
				status: Status = False
			else:
				status: Status = True
			msg: Msg = res_tokens[1]
			res: Response = (status, msg)
			return res
	except Exception as e:
		return (False, str(e))
		
		
main()	
