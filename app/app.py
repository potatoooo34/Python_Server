import socket  # noqa: F401
import threading

def parse_requests(req_data):
    lines = req_data.split('\r\n')
    method, path , version = lines[0].split(' ')

    if path == "/":
        response = "HTTP/1.1 200 OK\r\n\r\n"

    elif path.startswith("/echo/"):
        value = path.split("/echo/")[1]
        response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(value)}\r\n\r\n{value}"

    elif path == "/user-agent":
        useragent = lines[2].split(": ")[1]
        response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(useragent)}\r\n\r\n{useragent}"
        
    else:
        response = "HTTP/1.1 404 Not Found\r\n\r\n"

        

    return response




def handle_requests(client_socket):
    req_data = client_socket.recv(1024).decode()
    response = parse_requests(req_data)

    
    client_socket.send(response.encode())

def client_thread(conn , addr):
    print(f"Connection from {addr} extablished")
    handle_requests(conn)


def main():
    
    
    
    server_socket = socket.create_server(("localhost", 4221))
    server_socket.listen()
 
    try:
        while True:
            print("Waiting for a conection...")
            client_socket , addr = server_socket.accept()

            threading.Thread(target = client_thread , args = (client_socket , addr)).start()
            
            


    except KeyboardInterrupt:
        print("\n Server Shutting down")
    finally:
        server_socket.close()


if __name__ == "__main__":
    main()
