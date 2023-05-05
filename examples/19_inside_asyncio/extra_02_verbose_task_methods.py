import asyncio
from asyncio.tasks import _PyTask
from functools import wraps
from rich import print as rprint

from extra_01_decorator_verbose_methods_filter import verbose_methods_filter, time


def verbose_task(func):
    @wraps(func)
    def inner(*args, **kwargs):
        self = args[0]
        # min
        rprint(f"[violet]{time()} Calling {self.get_name():10} {func.__qualname__}")
        # more
        # rprint(f"[violet]Calling {func.__qualname__:30} {self.get_name()}\n\t{self}[/violet]")
        # args
        # rprint(f"[violet]Calling {func.__qualname__:30} {self.get_name()}\n\targs={args[1:]}[/violet]")
        result = func(*args, **kwargs)
        # rprint(f"[violet]Calling {func.__qualname__:30} {result=}")
        return result

    return inner


# all
# verbose_methods = verbose_methods_filter(ignore=["get_name", "set_name"], verbose=verbose_task)
# main
verbose_methods = verbose_methods_filter(
    include=["_Task__step", "_Task__wakeup"], verbose=verbose_task
)
# more
# verbose_methods = verbose_methods_filter(
#    include=["_Task__step", "_Task__wakeup", "add_done_callback"], verbose=verbose_task
# )


@verbose_methods
class CustomTask(_PyTask):
    def __init__(self, coro, *, loop=None, name=None):
        super().__init__(coro, loop=loop, name=name)
        rprint(f"[violet]{time()} Creating task {self}")


def task_factory(loop, coro):
    return CustomTask(coro, loop=loop)

