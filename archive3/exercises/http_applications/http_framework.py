import socket
from os import fork
from typing import Callable
from http_util import HTTPRequest, HTTPResponse

class HTTPFramework:
	def __init__(self):
		self.endpoints = {}

	def route(self, path: str, method: str):
		def decorator(func: Callable):
			self.endpoints[(method, path)] = func
		return decorator
		
	def get(self, path: str):
		return self.route(path, "GET")

	def put(self, path: str):
		return self.route(path, "PUT")

	def post(self, path: str):
		return self.route(path, "POST")

	def patch(self, path: str):
		return self.route(path, "PATCH")

	def delete(self, path: str):
		return self.route(path, "DELETE")

	def run(self, host, port):
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as s:
			s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
			s.bind((host, port))
			s.listen(5)
			while True:
				conn, addr = s.accept()
				if fork() == 0:
					with conn:
						try:
							request = HTTPRequest(conn.recv(1024).decode())
						except Exception as e:
							print(f"Exception {e}")
							request = None
						if request:
							req_func = self.endpoints.get((request.method, request.uri))
						else:
							req_func = None

						if req_func is None:
							res = HTTPResponse(404, "");
						else:
							res = req_func(request)
						conn.sendall(str(res).encode())
					exit(0)

if __name__ != '__main__':
	exit(0)

app = HTTPFramework()

@app.get("/")
def root(req: HTTPRequest) -> HTTPResponse:
	return HTTPResponse(200, "Hello")

@app.get("/hello")
def hello(req: HTTPRequest) -> HTTPResponse:
	res = HTTPResponse(200, "<p style='color: red'>Hello world</p>")
	return res
	
app.run('127.0.0.1', 8080)
