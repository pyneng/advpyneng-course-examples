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
        # rprint(f"[violet]Calling {self.get_name()} {func.__qualname__}")
        # rprint(f"[violet]Calling {func.__qualname__} {self.get_name()}\n{self}[/violet]")
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
            # if callable(method) and not re.search(r"__\S+__", name):
            if callable(method):
                methods[name] = method
        for name, method in methods.items():
            setattr(cls, name, verbose(method))
        return cls

    return verbose_methods


# verbose_methods = verbose_methods_filter()
verbose_methods = verbose_methods_filter(include=["_Task__step", "_Task__wakeup"])


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


@verbose_methods
class CustomTask(_PyTask):
    def __init__(self, coro, *, loop=None, name=None):
        super().__init__(coro, loop=loop, name=name)
        rprint(f"[violet]Creating task {self}")


def task_factory(loop, coro):
    return CustomTask(coro, loop=loop)


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.set_task_factory(task_factory)
    task1 = loop.run_until_complete(main())
    loop.close()
