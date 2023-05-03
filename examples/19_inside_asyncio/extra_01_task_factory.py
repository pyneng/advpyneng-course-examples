import asyncio
from datetime import datetime
from asyncio.tasks import _PyTask
from click import secho


def time():
    return datetime.now().time()


async def delay_msg(delay, msg):
    print(f"START delay_msg {msg=} {time()}")
    await asyncio.sleep(delay)
    print(f"STOP  delay_msg {msg=} {time()}")
    return msg


async def main():
    print(f">>> START MAIN {time()}")
    # res1 = await delay_msg(3, "task1")
    res1 = await asyncio.create_task(delay_msg(3, "task1"))
    print(f">>> STOP  MAIN {time()}")


class CustomTask(_PyTask):
    def __init__(self, coro, *, loop=None, name=None):
        super().__init__(coro, loop=loop, name=name)
        self._total_step = 0

    def _Task__step(self, exc=None):
        self._total_step += 1
        secho(f"==> STEP{self._total_step} {self.get_name().upper()} {self}", fg="green")
        super()._Task__step(exc=exc)
        secho(f"<== STEP{self._total_step} {self.get_name().upper()} {self}", fg="green")

    def __repr__(self):
        orig_repr = super().__repr__()
        return f"CustomTask {orig_repr}"


def task_factory(loop, coro):
    return CustomTask(coro, loop=loop)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.set_task_factory(task_factory)
    task1 = loop.run_until_complete(main())
    loop.close()
