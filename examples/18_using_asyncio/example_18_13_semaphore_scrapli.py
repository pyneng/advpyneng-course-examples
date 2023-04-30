import asyncio
import yaml
from pprint import pprint
from scrapli import AsyncScrapli
from scrapli.exceptions import ScrapliException


async def send_show(device, command, semaphore):
    try:
        async with semaphore:
            print(f"Connect {device['host']}")
            async with AsyncScrapli(**device) as ssh:
                response = await ssh.send_command(command)
                await asyncio.sleep(1)
                return response.result
    except ScrapliException as error:
        print(error)


async def run_all(devices, command):
    sem = asyncio.Semaphore(2)
    coroutines = [send_show(dev, command, sem) for dev in devices]
    results = await asyncio.gather(*coroutines, return_exceptions=True)
    return results


if __name__ == "__main__":
    with open("devices_scrapli_telnet.yaml") as f:
        devices = yaml.safe_load(f)
    output = asyncio.run(run_all(devices, "show ip int br"))
    print(output)

