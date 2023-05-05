import re
import asyncio
from extra_02_verbose_task_methods import task_factory
from extra_03_verbose_loop_methods import EventLoopPolicy


async def dummy():
    print(f"dummy start")
    await asyncio.sleep(5)
    # task = asyncio.create_task(asyncio.sleep(1))
    # await task
    print(f"dummy stop")


if __name__ == "__main__":
    asyncio.set_event_loop_policy(EventLoopPolicy())
    loop = asyncio.new_event_loop()
    loop.set_task_factory(task_factory)
    task1 = loop.run_until_complete(dummy())
    loop.close()
