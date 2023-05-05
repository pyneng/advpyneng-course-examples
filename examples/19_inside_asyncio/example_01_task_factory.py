import asyncio
from extra_02_verbose_task_methods import task_factory


async def hello():
    print("start hello")
    await asyncio.sleep(1)
    print("stop  hello")


async def main():
    print(f">>> START   MAIN")
    new_task = asyncio.create_task(hello())
    await new_task
    # await hello()
    print(f"<<< STOP    MAIN")


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.set_task_factory(task_factory)
    task1 = loop.run_until_complete(main())
    loop.close()
