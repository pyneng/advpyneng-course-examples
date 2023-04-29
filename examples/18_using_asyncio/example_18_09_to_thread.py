import asyncio
import time
from rich import print as rprint


def is_odd(number):
    return number % 2 == 1


def netmiko_connect(device):
    rprint(f"[green]sync Подключаюсь к {device}")
    time.sleep(5)
    rprint(f"[green]sync Получили результат {device}")


async def scrapli_connect(device):
    rprint(f"[violet]async Подключаюсь к {device}")
    await asyncio.sleep(1)
    rprint(f"[violet]async Получили результат {device}")


async def main():
    devices = list(range(10))
    coroutines = []
    for dev in devices:
        if is_odd(dev):
            coro = asyncio.to_thread(netmiko_connect, dev)
        else:
            coro = scrapli_connect(dev)
        coroutines.append(coro)
    await asyncio.sleep(5)
    print("coroutines")
    results = await asyncio.gather(*coroutines)
    return results


if __name__ == "__main__":
    asyncio.run(main())
