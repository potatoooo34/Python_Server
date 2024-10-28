import socket  # noqa: F401

def handle_requests(client_socket):
    client_socket.recv(1024)

    response = "HTTP/1.1 200 OK\r\n\r\n"
    client_socket.send(response.encode())


def main():
    
    
    
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
 
    try:
        while True:
            client_socket , addr = server_socket.accept()
            handle_requests(client_socket)


    except KeyboardInterrupt:
        print("\n Server Shutting down")
    finally:
        server_socket.close()


if __name__ == "__main__":
    main()
