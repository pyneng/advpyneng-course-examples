from pprint import pprint
import asyncio
import asyncssh

params = {"username": "cisco", "password": "cisco", "connect_timeout": 5}
hosts = ["192.168.139.1", "192.168.139.2", "192.168.139.13"]
devices = [{"host": ip, **params} for ip in hosts]
r1, r2, r3 = devices

ssh = await asyncssh.connect(**r1)
writer, reader, _ = await ssh.open_session()
await reader.readuntil(">")
writer.write("enable\n")
await reader.readuntil("Password")
writer.write("cisco\n")
await reader.readuntil("#")
writer.write("terminal length 0\n")
await reader.readuntil("#")


