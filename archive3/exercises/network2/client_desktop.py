from tkinter import *
import tkinter
from typing import NewType
from tkinter import ttk


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


def main():
	root = Tk()
	frm = ttk.Frame(root, padding=10)
	frm.grid()
	ttk.Button(frm, text="Login", command=login).grid(column=1, row=0)
	tkinter.simpledialog.askstring(title, "Username: ", **kw)
	tkinter.simpledialog.askstring(title, "Password: ", **kw)
	ttk.Button(frm, text="List Users", command=login).grid(column=1, row=0)
	ttk.Button(frm, text="Logout", command=login).grid(column=1, row=0)
	ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
	root.mainloop()

main()
