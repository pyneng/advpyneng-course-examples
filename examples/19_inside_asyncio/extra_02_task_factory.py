import asyncio
import re
from datetime import datetime
from asyncio.tasks import _PyTask
from functools import wraps
from rich import print as rprint


def verbose(func):
    @wraps(func)
    def inner(*args, **kwargs):
        self = args[0]
        rprint(f"[violet]Calling {func.__qualname__}\n{self}[/violet]")
        # print(f"Calling {func.__qualname__:30} args={args[1:]}")
        result = func(*args, **kwargs)
        # print(f"Calling {func.__qualname__:30} {result=}")
        return result

    return inner


def verbose_methods_filter(include=None, ignore=None):
    if ignore is None:
        ignore = set()
    if include is None:
        include = set()

    def verbose_methods(cls):
        all_attrs = set(dir(cls))
        if include:
            all_attrs = include
        elif ignore:
            all_attrs -= ignore
        methods = {}
        for name in all_attrs:
            method = getattr(cls, name)
            if callable(method) and not re.search(r"__\S+__", name):
                methods[name] = method
        for name, method in methods.items():
            setattr(cls, name, verbose(method))
        return cls

    return verbose_methods


# verbose_methods = verbose_methods_filter()
verbose_methods = verbose_methods_filter(include=["_Task__step", "_Task__wakeup"])


async def delay_msg(delay, msg):
    print(f"START delay_msg {msg=}")
    await asyncio.sleep(delay)
    print(f"STOP  delay_msg {msg=}")
    return msg


async def main():
    print(f">>> START   MAIN")
    # res = await delay_msg(3, "task1")
    await asyncio.sleep(3)
    print(f"<<< STOP    MAIN")


def task_factory(loop, coro):
    CustomTask = verbose_methods(_PyTask)
    return CustomTask(coro, loop=loop)


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.set_task_factory(task_factory)
    task1 = loop.run_until_complete(main())
    loop.close()
