import socket
from io import StringIO
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
fields = [
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

status_to_reason = {
	100: "Continue",
	101: "Switching Protocols",
	200: "OK",
	201: "Created",
	202: "Accepted",
	203: "Non-Authoritative Information",
	204: "No Content",
	205: "Reset Content",
	206: "Partial Content",
	300: "Multiple Choices",
	301: "Moved Permanently",
	302: "Found",
	303: "See Other",
	304: "Not Modified",
	305: "Use Proxy",
	307: "Temporary Redirect",
	400: "Bad Request",
	401: "Unauthorized",
	402: "Payment Required",
	403: "Forbidden",
	404: "Not Found",
	405: "Method Not Allowed",
	406: "Not Acceptable",
	407: "Proxy Authentication Required",
	408: "Request Time-out",
	409: "Conflict",
	410: "Gone",
	411: "Length Required",
	412: "Precondition Failed",
	413: "Request Entity Too Large",
	414: "Request-URI Too Large",
	415: "Unsupported Media Type",
	416: "Requested range not satisfiable",
	417: "Expectation Failed",
	500: "Internal Server Error",
	501: "Not Implemented",
	502: "Bad Gateway",
	503: "Service Unavailable",
	504: "Gateway Time-out",
	505: "HTTP Version not supported",
}

versions = ["HTTP/1.1"]

@dataclass 
class Header:
	field: str
	value: str

class HTTPRequest:
	def __init__(self, request: str):
		self.method: str
		self.uri: str
		self.version: str
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
		headers = StringIO()
		for header in self.headers:
			headers.write(f"{header.field}: {header.value}\r\n")
		headers = headers.getvalue()
		return (f"{self.method} {self.uri}\r\n"
				f"{headers}\r\n"
				f"{self.body}"
				)

	def __parse_request_line(self) -> bool:
		if not self.scanner.has_next_line():
			self.parse_error = "No request line"
			return False
		request_line = self.scanner.get_next_line()
		request_line_parts = request_line.split()
		if not 2 <= len(request_line_parts) <= 3:
			self.parse_error = "Malformed request line: Not enough parts"
			return False
		method = request_line_parts[0].upper()
		if method not in methods:
			self.parse_error = "Invalid Method"
			return False
		if len(request_line_parts) == 3:
			version = request_line_parts[2]
			if version not in versions:
				self.parse_error = "Invalid Version"
				return False
		else:
			version = "HTTP/1.1"
		self.version = version
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
			field = parts[0]
			value = parts[1]
			self.headers.append(Header(field, value))
		return True
			
	def __parse_body(self) -> bool:
		body = []
		while self.scanner.has_next_line():
			body.append(self.scanner.get_next_line())
		self.body = "\n".join(body)
		return True

class HTTPResponse:
	def __init__(self, status_code: int, body: str, headers: dict[str, str] = None, version: str = "HTTP/1.1"):
		self.status_code = status_code
		self.headers = headers or {}
		self.body = body
		self.version = version

		if "Content-Length" not in self.headers:
			self.headers["Content-Length"] = len(body)

	def __str__(self):
		reason_phrase = status_to_reason[self.status_code]
		headers = StringIO()
		for k, v in self.headers.items():
			headers.write(f"{k}: {v}\r\n")
		return (f"{self.version} {self.status_code} {reason_phrase}\r\n"
				f"{headers.getvalue()}\r\n"
				f"{self.body}"
		)


		

if __name__ == '__main__':
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
