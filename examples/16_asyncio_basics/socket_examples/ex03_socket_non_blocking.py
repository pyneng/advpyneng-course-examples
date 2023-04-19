import socket
import time


def create_server(address, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.setblocking(False) # non-blocking
    server_socket.bind((address, port))
    server_socket.listen()
    return server_socket


def accept_client(server_socket):
    client_socket, client_address = server_socket.accept()
    client_socket.setblocking(False) # non-blocking
    print(f"{client_socket=}")
    return client_socket


def recv_and_send(client_socket):
    data = client_socket.recv(100)
    print(f"{data=}")
    client_socket.send(data.upper())
    if b"close" in data:
        client_socket.close()
        client_sockets_list.remove(client_socket)


server_socket = create_server("localhost", 8080)
client_sockets_list = []

try:
    while True:
        print("Waiting ...")
        try:
            client_socket = accept_client(server_socket)
        except BlockingIOError:
            print("No client")
        else:
            client_sockets_list.append(client_socket)
        for cl_s in client_sockets_list:
            try:
                recv_and_send(cl_s)
            except BlockingIOError:
                print("No data")
        time.sleep(0.5)

finally:
    server_socket.close()
