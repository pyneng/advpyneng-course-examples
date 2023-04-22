import asyncio
from pprint import pprint
import random
from rich import inspect


async def send_show(device, show):
    print(f"Start send_show {device=}")
    await asyncio.sleep(random.random() * 3)
    print(f"Send  command {show=} {device=}")
    if device == 3:
        raise ValueError
    await asyncio.sleep(random.random() * 3)
    print(f"End   send_show  {device=}")
    return f"{device} {show}"


async def get_show_from_devices(devices, command):
    result_dict = {}
    coroutines = [send_show(dev, command) for dev in devices]
    results = await asyncio.gather(*coroutines, return_exceptions=True)
    print(f"{results=}")
    for dev, result in zip(devices, results):
        if isinstance(result, Exception):
            print(f"На устройстве {dev=} возникло исключение {result=}")
        else:
            print(f"{dev=} {result=}")
            result_dict[dev] = result
    return result_dict



if __name__ == "__main__":
    r_dict = asyncio.run(get_show_from_devices([1, 2, 3, 4, 5], "sh clock"))
    pprint(r_dict)
