import socket


def create_server(address, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((address, port))
    server_socket.listen()
    return server_socket


server_socket = create_server("localhost", 9000)


while True:
    print("Waiting accept...")
    client_socket, client_address = server_socket.accept()
    print(f"{client_socket=}")
    print(f"{client_address=}")

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
    print(f"client done {client_address=}")
