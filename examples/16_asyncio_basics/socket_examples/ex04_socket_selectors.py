import socket
import selectors


def create_server(address, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((address, port))
    server_socket.listen()
    return server_socket


def accept_client(server_socket):
    client_socket, client_address = server_socket.accept()
    print(f"{client_socket=}")
    return client_socket


def recv_and_send(client_socket):
    data = client_socket.recv(100)
    print(f"{data=}")
    client_socket.send(data.upper())
    if b"close" in data:
        client_socket.close()
        selector.unregister(client_socket)


server_socket = create_server("localhost", 8080)
selector = selectors.DefaultSelector()
selector.register(server_socket, selectors.EVENT_READ)

try:
    while True:
        print("Waiting ...")
        new_events = selector.select()
        for event, _ in new_events:
            event_socket = event.fileobj

            if event_socket is server_socket:
                client_socket = accept_client(server_socket)
                selector.register(client_socket, selectors.EVENT_READ)
            else:
                recv_and_send(event_socket)

finally:
    server_socket.close()
