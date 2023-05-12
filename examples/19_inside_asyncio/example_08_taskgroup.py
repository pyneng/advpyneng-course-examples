import asyncio
from pprint import pprint
from scrapli import AsyncScrapli
from scrapli.exceptions import ScrapliException
import yaml



async def send_show(device, command):
    host = device["host"]
    if host == "192.168.139.1":
        raise ValueError
    elif host == "192.168.139.2":
        raise TypeError
    async with AsyncScrapli(**device) as ssh:
        response = await ssh.send_command(command)
        return response.result



async def run_all(devices, command):
    async with asyncio.TaskGroup() as tg:
        tasks = [tg.create_task(send_show(dev, command)) for dev in devices]
    results = [t.result() for t in tasks]
    return results



if __name__ == "__main__":
    with open("devices_scrapli.yaml") as f:
        devices = yaml.safe_load(f)
    output = asyncio.run(run_all(devices, "show clock"))
    print(output)
