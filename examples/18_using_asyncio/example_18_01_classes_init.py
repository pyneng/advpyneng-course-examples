from pprint import pprint
import asyncio
import asyncssh


class CiscoAsyncSSH:
    def __init__(self, host, username, password, enable_password):
        self.host = host
        self.username = username
        self.password = password
        self.enable_password = enable_password
        self._ssh = None

    async def connect(self):
        if self._ssh is not None:
            return
        self._ssh = await asyncssh.connect(
            self.host,
            username=self.username,
            password=self.password,
            connect_timeout=5,
        )
        self._writer, self._reader, _ = await self._ssh.open_session()
        await self._readuntil(">")
        self._writer.write("enable\n")
        await self._readuntil("Password")
        self._writer.write(f"{self.enable_password}\n")
        await self._readuntil("#")
        self._writer.write("terminal length 0\n")
        await self._readuntil("#")

    async def _readuntil(self, prompt, timeout=3):
        output = await asyncio.wait_for(self._reader.readuntil(prompt), timeout=timeout)
        return output

    async def send_show_command(self, command):
        self._writer.write(f"{command}\n")
        output = await self._readuntil("#")
        return output

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self._ssh.close()


async def send_show(device, show):
    async with CiscoAsyncSSH(**device) as r1:
        output = await r1.send_show_command(show)
        return output


async def send_command_to_devices(devices, show):
    coroutines = [send_show(dev, show) for dev in devices]
    results = await asyncio.gather(*coroutines)
    return results


if __name__ == "__main__":
    params = {"username": "cisco", "password": "cisco", "enable_password": "cisco"}
    hosts = ["192.168.139.1", "192.168.139.2", "192.168.139.3"]
    devices = [{"host": ip, **params} for ip in hosts]
    pprint(asyncio.run(send_command_to_devices(devices, "sh ip int br")))

