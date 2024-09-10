import socket

"""
HTTP Protocol Example

See https://datatracker.ietf.org/doc/html/rfc2616#section-6 for formatting
"""

msg = [
(
"HTTP/1.1 200 OK\r\n"
"Content-Type: text/plain\r\n"
"Content-Length: 5\r\n"
"\r\n"
"Hello"
),
("HTTP/1.1 200 OK\r\n"
"Content-Type: text/plain\r\n"
"Content-Length: 37\r\n"
"\r\n"
"<p style='color: red'>Hello world</p>"
),
("HTTP/1.1 200 OK\r\n"
"Content-Type: text/html\r\n"
"Content-Length: 37\r\n"
"\r\n"
"<p style='color: red'>Hello world</p>"
),
] 

prompt =  	("Which Response would you like to send?\n"
			"1. HTTP Plain Text\n"
			"2. HTTP Plain Text with HTML format\n"
			"3. HTTP with HTML encoding and HTML format\n")

res = msg[int(input(prompt)) - 1]

host = '127.0.0.1'
port = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as s:
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.bind((host, port))
	s.listen(1)
	print("Server running at %s:%d" % (host, port))
	while True:
		conn, addr = s.accept()
		with conn:
			data = conn.recv(1024).decode()
			if data:
				conn.sendall(res.encode())
