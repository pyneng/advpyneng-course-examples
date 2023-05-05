import asyncio
from pprint import pprint
from random import random


async def send_show(device, command):
    print(f"Подключаюсь к {device}")
    try:
        await asyncio.sleep(random() * 3)
        print(f"Inside {device}")
        await asyncio.sleep(2)
        print(f"Done {device}")
        return f"RESULT {device} {command}"
    except asyncio.CancelledError:
        print(f"Отмена... {device}")
        await asyncio.sleep(2)
        print("Отменено")
        raise


async def cancel_tasks():
    tasks = [task for task in asyncio.all_tasks() if task is not asyncio.current_task()]
    [task.cancel() for task in tasks]
    output = await asyncio.gather(*tasks, return_exceptions=True)
    print(f"{output=}")
    return output


async def run_all(devices, command):
    tasks = [asyncio.create_task(send_show(dev, command)) for dev in devices]
    results = []
    for task in tasks:
        try:
            res = await task
            results.append(res)
        except asyncio.CancelledError:
            print(f"Cancelled {task}")
            # output = await cancel_tasks()
            # print(f"{output=}")
    print(f"{results=}")
    return results


if __name__ == "__main__":
    devices = range(1, 11)
    try:
        output = asyncio.run(run_all(devices, "sh clock"))
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
