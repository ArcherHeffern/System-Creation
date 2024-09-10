from sock_util import *
import signal

signal.signal(signal.SIGINT, lambda *x: exit(0))

print("`help` for a help menu")
s = server_connect("127.0.0.1", 8080)
while True:
    # User Interface
    user_input = input("> ")
    if user_input == "exit":
        break

    s.sendall(user_input.encode())
    remote_result = s.recv(1024).decode()
    print(f"Remote: {remote_result}")
server_close(s)
print("Exiting...")
