import socket


def create_server(address, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((address, port))
    server_socket.listen()
    return server_socket


def accept(server_socket):
    print("Waiting accept...")
    client_socket, client_address = server_socket.accept()
    print(f"{client_socket=}")
    print(f"{client_address=}")
    return client_socket


def recv_and_send(client_socket):
    client_data = b""
    while True:
        if b"close" in client_data:
            client_socket.close()
            break
        else:
            data = client_socket.recv(4096)  # blocking
            print(f"{data=}")
            client_data += data

        client_socket.send(data.upper())
    print(f"client done")


server_socket = create_server("localhost", 8080)


while True:
    client_socket = accept(server_socket)
    recv_and_send(client_socket)
