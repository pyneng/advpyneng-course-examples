import asyncio
import time
import random
from rich import print as rprint


def is_odd(number):
    return number % 2 == 1


def netmiko_connect(device):
    rprint(f"[red]sync  {device:<4} start")
    time.sleep(random.random() * 3)
    rprint(f"[red]sync  {device:<4} end")


async def scrapli_connect(device):
    rprint(f"[green]async {device:<4} start")
    await asyncio.sleep(random.random() * 3)
    rprint(f"[green]async {device:<4} end")


async def main():
    devices = range(100)
    coroutines = []
    for dev in devices:
        if is_odd(dev):
            c = asyncio.to_thread(netmiko_connect, dev)
        else:
            c = scrapli_connect(dev)
        coroutines.append(c)
    results = await asyncio.gather(*coroutines)
    return results



if __name__ == "__main__":
    asyncio.run(main())
