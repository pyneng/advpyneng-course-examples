import asyncio
import random
from pprint import pprint
from functools import wraps
import yaml


async def limited_run(semaphore, coro):
    async with semaphore:
        return await coro


async def send_show(device, command):
    print(f">>> Connect SHOW {device}")
    await asyncio.sleep(random.random())
    print(f"<<< Done    SHOW {device}")
    return f"SHOW {device=} {command=}"


async def send_cfg(device, command):
    print(f">>> Connect CFG {device}")
    await asyncio.sleep(random.random() * 2)
    print(f"<<< Done    CFG {device}")
    return f"CFG {device=} {command=}"


async def run_all(devices, show, cfg, limit=8):
    semaphore1 = asyncio.Semaphore(limit)
    semaphore2 = asyncio.Semaphore(limit)
    # coros = [send_show(dev, show) for dev in devices]
    coros1 = [limited_run(semaphore1, send_show(dev, show)) for dev in devices]
    coros2 = [limited_run(semaphore2, send_cfg(dev, cfg)) for dev in devices]
    results = await asyncio.gather(*coros1, *coros2, return_exceptions=True)
    return results


if __name__ == "__main__":
    devices = range(10)
    output = asyncio.run(run_all(devices, "show ip int br", "alias exec c conf t"))
    pprint(output)
