import asyncio
import random
from pprint import pprint
from functools import wraps
import yaml


async def limited_gather(*coroutines, limit, return_exceptions=False):
    semaphore = asyncio.Semaphore(limit)

    async def limited_run(coro):
        async with semaphore:
            return await coro

    return await asyncio.gather(
        *(limited_run(coro) for coro in coroutines),
        return_exceptions=return_exceptions,
    )


async def send_show(device, command):
    host = device
    print(f">>> Connect {host}")
    await asyncio.sleep(random.random())
    print(f"<<< Done    {host}")
    return f"SHOW {host=} {command=}"


async def send_cfg(device, command):
    host = device
    print(f">>> Connect CFG {host}")
    await asyncio.sleep(random.random() * 2)
    print(f"<<< Done    CFG {host}")
    return f"CFG {host=} {command=}"


async def run_all(devices, show, cfg):
    coroutines1 = [send_show(dev, show) for dev in devices]
    coroutines2 = [send_cfg(dev, cfg) for dev in devices]
    coros = coroutines1 + coroutines2
    results = await limited_gather(*coros, limit=5, return_exceptions=True)
    return results


if __name__ == "__main__":
    devices = range(10)
    output = asyncio.run(run_all(devices, "show ip int br", "alias exec c conf t"))
    pprint(output)
