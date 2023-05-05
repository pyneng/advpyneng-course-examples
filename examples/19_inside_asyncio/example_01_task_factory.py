import asyncio
from extra_02_verbose_task_methods import task_factory


async def main():
    print(f">>> START   MAIN")
    await asyncio.gather(asyncio.sleep(1))
    print(f"<<< STOP    MAIN")


if __name__ == "__main__":
    # asyncio.run(main())
    loop = asyncio.new_event_loop()
    loop.set_task_factory(task_factory)
    loop.run_until_complete(main())
    loop.close()
