import asyncio
import time
from pprint import pprint
from random import random


async def send_show(device, command):
    print(f"Подключаюсь к {device}")
    try:
        await asyncio.sleep(random() * 3)
    except asyncio.CancelledError:
        print(f"Отмена... {device}")
        await asyncio.sleep(2)
        print("Отменено")
        raise
    print(f"Done {device}")
    return f"RESULT {device} {command}"


async def run_all(devices, command):
    coroutines = [send_show(dev, command) for dev in devices]
    results = []
    results = await asyncio.gather(*coroutines, return_exceptions=True)
    return results


if __name__ == "__main__":
    devices = range(1, 6)
    try:
        output = asyncio.run(run_all(devices, "sh clock"))
    except KeyboardInterrupt:
        pass
