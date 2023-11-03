import socket

# Define the host and port to listen on
# Use '0.0.0.0' to listen on all available network interfaces
host = input("Server IP (default 127.0.0.1): ") or '127.0.0.1'
port = int(input("Server Port (default 8080): ") or 8080)

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Listen for incoming connections
client_socket.connect((host, port))

print(f"Client is connected to {host}:{port}")

while True:
    message = input(">>> ")
    client_socket.send(message.encode())

    data = client_socket.recv(1024)
    if not data:
        print("Connected was closed by the server")
        break
    print("Received from server: ", data.decode())

    # Check if the connection is still alive
    try:
        # Sending a probe to see if the server is still responding
        client_socket.send(b'')
    except socket.error as e:
        print("Connection closed by the server")
        break

# Close the server socket
client_socket.close()
