import asyncio
import yaml
from pprint import pprint
from scrapli import AsyncScrapli
from scrapli.exceptions import ScrapliException


async def send_show(device, command):
    try:
        async with AsyncScrapli(**device) as ssh:
            response = await ssh.send_command(command)
            return response.result
    except ScrapliException as error:
        print(error)


async def run_all(devices, command):
    coroutines = [send_show(dev, command) for dev in devices]
    results = await asyncio.gather(*coroutines, return_exceptions=True)
    return results


async def run_all(devices, command):
    results = []
    coroutines = [send_show(dev, command) for dev in devices]
    for coro in asyncio.as_completed(coroutines):
        res = await coro
        results.append(res)
    return results


if __name__ == "__main__":
    with open("devices_scrapli.yaml") as f:
        devices = yaml.safe_load(f)
    output = asyncio.run(run_all(devices, "show clock"))
    print(output)
