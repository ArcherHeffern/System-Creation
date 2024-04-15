import socket
from pprint import PrettyPrinter as PP
from dataclasses import dataclass, field

pp = PP()

"""
HTTP Protocol Example

See https://datatracker.ietf.org/doc/html/rfc2616#section-6 for formatting

This example processes the client request and calls the corresponding function
"""

host = ''
port = 8080

class Scanner:
	def __init__(self, string: str):
		self.strings: list[str] = string.split("\n")
		self.line: int = 1

	def has_next_line(self):
		return self.line < len(self.strings)

	def peek_line(self):
		return self.strings[self.line - 1]

	def get_next_line(self) -> str:
		self.line += 1
		return self.strings[self.line - 2]

methods = ["GET", "PUT", "POST", "PATCH", "DELETE", "HEAD", "OPTIONS", "TRACE", "CONNECT"]
header_fields = [
	"Accept",
	"Accept-Charset",
	"Accept-Encoding",
	"Accept-Language",
	"Authorization",
	"Expect",
	"From",
	"Host",
	"If-Match",
	"If-None-Match",
	"If-Range",
	"If-Unmodified-Since",
	"Max-Forwards",
	"Proxy-Authorization",
	"Range",
	"Referer",
	"TE",
	"User-Agent",
]

@dataclass 
class Header:
	header_field: str
	header_value: str

@dataclass
class HTTPRequest:

	def __init__(self, request: str):
		self.method: str
		self.uri: str
		self.body: str
		self.headers: list[Header] = []
		self.parse_error: str|None = None
		self.scanner = Scanner(request)
		if not self.__parse_request_line():
			raise Exception(self.parse_error)
		if not self.__parse_headers():
			raise Exception(self.parse_error)
		if not self.__parse_body():
			raise Exception(self.parse_error)

	def __str__(self):
		return (f"{self.method} {self.uri}"
				f"{pp.pprint(list(header for header in self.headers))}"
				f"{self.body}"
				)

	def __parse_request_line(self) -> bool:
		if self.scanner.has_next_line():
			request_line = self.scanner.get_next_line()
			request_line_parts = request_line.split()
			if len(request_line_parts) != 3:
				self.parse_error = "Malformed request line: Not enough parts"
				return False
			method = request_line_parts[0].upper()
			if method not in methods:
				self.parse_error = "Invalid Method"
				return False
			self.method = method
			self.uri = request_line_parts[1]
			return True

	def __parse_headers(self) -> bool:
		while self.scanner.has_next_line():
			line = self.scanner.get_next_line().strip()
			if line == "":
				return True
			parts = list(map(str.strip, line.split(":", maxsplit=1)))
			if len(parts) != 2:
				self.parse_error = f"Malformed header field [{line}]"
				return False
			header_field = parts[0]
			header_value = parts[1]
			self.headers.append(Header(header_field, header_value))
		return True
			
	def __parse_body(self) -> bool:
		body = []
		while self.scanner.has_next_line():
			body.append(self.scanner.get_next_line())
		self.body = "\n".join(body)
		return True

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as s:
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.bind((host, port))
	s.listen(1)
	while True:
		conn, addr = s.accept()
		with conn:
			request = HTTPRequest(conn.recv(1024).decode())
			print(request)
			res = (
			"HTTP/1.1 200 OK\r\n"
			"Content-Type: text/plain; charset=utf-8\r\n"
			"Content-Length: 5\r\n"
			"\r\n"
			"Hello"
			)
			conn.sendall(res.encode())
