import socket


def main():
    # Define the host and port to listen on
    host = '127.0.0.1'  # Use '0.0.0.0' to listen on all available network interfaces
    port = 8080

    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the host and port
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(1)  # Listen for up to 5 connections

    print(f"Server is listening on {host}:{port}")

    # Accept a connection from a client
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    while True:

        # Receive data from the client (up to 1024 bytes)
        data = client_socket.recv(1024)
        if not data:
            break  # If no data is received, exit the loop

        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
        # Process the received data (you can replace this with your own logic)
        client_request = data.decode('utf-8')
        server_response = MailProtocol.process_request(client_request)
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#

        # Send a response to the client
        client_socket.send(server_response.encode('utf-8'))

    # Close the client socket
    client_socket.close()
    # Close the server socket
    server_socket.close()


class MailProtocol:
    # You will implement this method
    @staticmethod
    def process_request(request: str) -> str:
        return f"Server recieved {request}"


if __name__ == '__main__':
    main()
