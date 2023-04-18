import socket


def create_server(address, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((address, port))
    server_socket.listen()
    return server_socket


server_socket = create_server("localhost", 8080)


try:
    print("Waiting accept...")
    client_socket, client_address = server_socket.accept()
    print(f"{client_socket=}")
    print(f"{client_address=}")

    while True:
        data = client_socket.recv(100)
        print(f"{data=}")
        client_socket.send(data.upper())
        if b"close" in data:
            break

    client_socket.close()
finally:
    server_socket.close()
