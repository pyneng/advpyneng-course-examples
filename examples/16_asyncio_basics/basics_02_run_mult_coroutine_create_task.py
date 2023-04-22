import asyncio
from pprint import pprint
import random


async def send_show(device, show):
    print(f"Start send_show {device=}")
    await asyncio.sleep(random.random() * 3)
    print(f"Send  command {show=} {device=}")
    await asyncio.sleep(random.random() * 3)
    print(f"End   send_show  {device=}")
    return f"{device} {show}"


async def get_show_from_devices(devices, command):
    tasks = [asyncio.create_task(send_show(dev, command)) for dev in devices]
    results = [await task for task in tasks]
    return results


if __name__ == "__main__":
    command_output = asyncio.run(get_show_from_devices([1, 2, 3], "sh clock"))
