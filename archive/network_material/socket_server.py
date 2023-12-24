import socket

# Define the host and port to listen on
host = '0.0.0.0'
port = 8080

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(5)  # Listen for up to 5 connections

print(f"Server is listening on {host}:{port}")

while True:
    # Accept a connection from a client
    client_socket, client_address = server_socket.accept()

    print(f"Accepted connection from {client_address}")

    # Handle the connection
    # Receive data from the client (up to 1024 bytes)
    data = client_socket.recv(1024)
    if not data:
        break  # If no data is received, exit the loop

    # Process the received data (you can replace this with your own logic)
    response = f"Server received: {data.decode('utf-8')}"
    print(response)
    # Send a response to the client
    client_socket.send(response.encode('utf-8'))

    # Close the client socket
    client_socket.close()

# Close the server socket
server_socket.close()
