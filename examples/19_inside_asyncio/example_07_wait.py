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
    except asyncio.CancelledError:
        print("Cancelled START")
        await asyncio.sleep(2)
        print("Cancelled STOP")
        raise


async def run_all(devices, command):
    coroutines = [send_show(dev, command) for dev in devices]
    results = await asyncio.gather(*coroutines, return_exceptions=True)
    return results


async def run_all(devices, command):
    tasks = [asyncio.create_task(send_show(dev, command)) for dev in devices]
    done_set, pending_set = await asyncio.wait(
        tasks, timeout=10, return_when=asyncio.ALL_COMPLETED
    )
    pprint(done_set)
    pprint(pending_set)
    [t.cancel() for t in pending_set]
    # results = [await t for t in done_set]
    results = [t.result() for t in done_set]
    return results


if __name__ == "__main__":
    with open("devices_scrapli.yaml") as f:
        devices = yaml.safe_load(f)
    output = asyncio.run(run_all(devices, "show clock"))
    print(output)
