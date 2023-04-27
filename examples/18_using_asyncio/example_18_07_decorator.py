import asyncio
from pprint import pprint
from functools import wraps
import inspect
import yaml
from scrapli import AsyncScrapli
from scrapli.exceptions import ScrapliException


def verbose(func):
    print(f"verbose {func=}")

    if inspect.iscoroutinefunction(func):
        @wraps(func)
        async def inner(*args, **kwargs):
            print(f"inner {args=} {kwargs=}")
            result = await func(*args, **kwargs)
            print(f"inner {result=}")
            return result

        return inner
    else:
        @wraps(func)
        def inner(*args, **kwargs):
            print(f"inner {args=} {kwargs=}")
            result = func(*args, **kwargs)
            print(f"inner {result=}")
            return result

        return inner


@verbose # send_show = verbose(send_show)
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


if __name__ == "__main__":
    with open("devices_scrapli_telnet.yaml") as f:
        devices = yaml.safe_load(f)
    output = asyncio.run(run_all(devices, "show clock"))
    pprint(output)
