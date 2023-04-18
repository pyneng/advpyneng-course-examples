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

    client_data = b""

    while b"close" not in client_data:
        part = client_socket.recv(1)
        print(f"{part=}")
        client_data += part
    print(f"{client_data=}")

    client_socket.send(client_data.upper())
    client_socket.close()
finally:
    server_socket.close()
