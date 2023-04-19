import telnetlib
import time
import random
from concurrent.futures import ThreadPoolExecutor


def client(client_id):
    telnet = telnetlib.Telnet("127.0.0.1", port=8080)
    print(f"{client_id=} connected")
    telnet.write(f"CLIENT {client_id}".encode() + b"\r\n")
    output = telnet.read_until(str(client_id).encode())
    print(f"{output=}")
    telnet.write(b"close\r\n")


with ThreadPoolExecutor(10) as ex:
    futures = [ex.submit(client, i) for i in range(1, 11)]
    [f.result() for f in futures]
