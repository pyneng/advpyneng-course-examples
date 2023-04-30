import asyncio
import random


async def send_show(device, command, semaphore):
    print("^^^ Waiting")
    async with semaphore:
        print(f">>> Connect {device}")
        await asyncio.sleep(random.random() * 3)
        print(f"<<< Done    {device}")


async def main():
    s = asyncio.Semaphore(10)
    coroutines = [send_show(i, "sh clock", s) for i in range(50)]
    await asyncio.gather(*coroutines)


if __name__ == "__main__":
    asyncio.run(main())

