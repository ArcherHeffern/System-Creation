import socket

"""
HTTP Protocol Example

See https://datatracker.ietf.org/doc/html/rfc2616#section-6 for formatting
"""

host = ''
port = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as s:
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.bind((host, port))
	s.listen(1)
	while True:
		conn, addr = s.accept()
		with conn:
			data = conn.recv(1024).decode()
			if data:
				res = (
				"HTTP/1.1 200 OK\r\n"
				"Content-Type: text/plain; charset=utf-8\r\n"
				"Content-Length: 5\r\n"
				"\r\n"
				"Hello"
				)
				conn.sendall(res.encode())
