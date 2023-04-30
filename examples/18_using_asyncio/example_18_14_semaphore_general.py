import asyncio
import yaml
from pprint import pprint
from scrapli import AsyncScrapli
from scrapli.exceptions import ScrapliException


async def semaphore_connect(semaphore, func, *args, **kwargs):
    async with semaphore:
        return await func(*args, **kwargs)


async def send_show(device, command):
    try:
        async with AsyncScrapli(**device) as ssh:
            print(f"Connect {device['host']}")
            # await asyncio.sleep(1)
            response = await ssh.send_command(command)
            return response.result
    except ScrapliException as error:
        print(error)


async def run_all(devices, command):
    sem = asyncio.Semaphore(2)
    coroutines = [semaphore_connect(sem, send_show, dev, command) for dev in devices]
    results = await asyncio.gather(*coroutines, return_exceptions=True)
    return results


if __name__ == "__main__":
    with open("devices_scrapli_telnet.yaml") as f:
        devices = yaml.safe_load(f)
    output = asyncio.run(run_all(devices, "show ip int br"))
    print(output)
