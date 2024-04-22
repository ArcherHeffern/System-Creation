import socket
from os import fork
from datetime import datetime
from typing import NewType
from dataclasses import dataclass, field

"""
Remote Procedure call approach

Def not the most efficient data structures for certain operations - But very bare bones
"""

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 8080              # Arbitrary non-privileged port

NOT_ENOUGH_ARGS = "Not enough arguments, expected %d"

Status = NewType('Status', bool)
Msg = NewType('Msg', str)
Response = NewType('Response', tuple[Status, Msg])

@dataclass
class Token:
	val: str
	expiration_date: datetime

@dataclass 
class GroupChat:
	chat_name: str

@dataclass
class Chat:
	author: 'User'
	msg: str

@dataclass
class User:
	username: str
	password: str
	group_chats: list[GroupChat] = field(default_factory = list)
	tokens: list[Token] = field(default_factory = list)

users: list[User] = set()

def __get_user(username):
	for user in users:
		if user.username == username:
			return user

def __user_exists(username):
	return any(user.username == username for user in users)

def __generate_token(user: User) -> str:
	token = len(user.tokens) + 1
	user.tokens.append(token)
	return token

def __password_authenticate(username: str, password: str) -> None|Response:
	if not __user_exists(username):
		return (False, "User not found")
	user = __get_user(username)
	if user.password == password:
		return (True, "Correct Password")
	return None

def __authenticate(username: str, token: str) -> None|Response:
	if not __user_exists(username):
		return (False, "User not found")
	user = __get_user(username)
	token = filter(lambda t: t.val == token, user.tokens)[:1]
	if not token:
		return (False, "Invalid token")
	if token.expiration_date < datetime.datetime.today():
		return (False, "Invalid token")
	return None
	

def list_users(tokens) -> Response:
	if len(tokens) < 2:
		return (False, NOT_ENOUGH_ARGS)
	username = tokens[1]
	token = tokens[2]
	if auth := __authenticate(username, token) is not None:
		return auth
	user_names = []
	for user in users:
		user_names.append(user.username)
	return (True, json.dumps(user_names))
		

def create_account(tokens):
	if len(tokens) < 4:
		return (False, NOT_ENOUGH_ARGS % 4)
	username = tokens[1]
	password = tokens[2]
	if any(user.name == tokens.username for user in users):
		return (False, "Username already exists")
	users.append(User(username, password))
	return (True, "User successfully created")

def login(tokens):
	if len(tokens) < 3:
		return (False, NOT_ENOUGH_ARGS % 3)
	username = tokens[1]
	password = tokens[2]
	if not (res := __password_authenticate(username, password)):
		return res
	user = __get_user(username)
	token = __generate_token(user)
	return token

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT))
	s.listen(5)
	while True:
		conn, addr = s.accept()
		if fork() == 0:
			with conn:
				print('Connected by', addr)
				data = conn.recv(1024).decode()
				if not data: break
				tokens = data.split()
				command = tokens[0]
				match command:
					case "login":
						res = login(tokens)
					case "create_account":
						res = create_account(tokens)
					case "list_users":
						res = list_users(tokens)
					case default:
						res = (False, f"Command {default} not found")
				conn.sendall((f"{res[0]} {res[1]}").encode())
				exit(0)
			
