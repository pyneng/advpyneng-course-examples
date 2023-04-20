import asyncio
from datetime import datetime


async def delay_msg(delay, msg):
    print(f"START delay_msg {msg=} {datetime.now()}")
    await asyncio.sleep(delay)
    print(f"STOP  delay_msg {msg=} {datetime.now()}")
    return msg


async def main():
    print(f">>> START {datetime.now()}")
    task1 = asyncio.create_task(delay_msg(5, "task1"))
    task2 = asyncio.create_task(delay_msg(4, "task2"))
    print(f">>> All tasks running {task1=}")
    res1 = await task1
    res2 = await task2
    print(f">>> STOP  {datetime.now()}")
    print(f"{res1=} {res2=}")


async def main2():
    print(f">>> START {datetime.now()}")
    res1 = await delay_msg(5, "task1")
    res2 = await delay_msg(4, "task2")
    print(f">>> STOP  {datetime.now()}")
    print(f"{res1=} {res2=}")


if __name__ == "__main__":
    asyncio.run(main())
