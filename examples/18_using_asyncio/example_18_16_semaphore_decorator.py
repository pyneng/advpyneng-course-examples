import asyncio
import random
from pprint import pprint
from functools import wraps
import yaml


def create_semaphore(semaphore):
    def s_decorator(func):
        @wraps(func)
        async def inner(*args, **kwargs):
            async with semaphore:
                return await func(*args, **kwargs)

        return inner

    return s_decorator


limit1 = create_semaphore(asyncio.Semaphore(5))
limit2 = create_semaphore(asyncio.Semaphore(5))


@limit1
async def send_show(device, command):
    host = device
    print(f">>> Connect {host}")
    await asyncio.sleep(random.random() * 3)
    print(f"<<< Done    {host}")
    return f"SHOW {host=} {command=}"


@limit2
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
    random.shuffle(coros)

    results = await asyncio.gather(*coros, return_exceptions=True)
    return results


if __name__ == "__main__":
    devices = range(10)
    output = asyncio.run(run_all(devices, "show ip int br", "alias exec c conf t"))
    pprint(output)
