import asyncio
from asyncio.events import BaseDefaultEventLoopPolicy as BasePolicy
from rich import inspect
from click import secho
from functools import wraps
from extra_02_task_factory import task_factory


def verbose(func):
    @wraps(func)
    def inner(*args, **kwargs):
        self = args[0]
        print(f">>> VERBOSE {func.__qualname__:30} args={args[1:]}")
        if len(self._scheduled):
            print(f"    {self._scheduled=}")
        if len(self._ready):
            print(f"    {self._ready=}")
        result = func(*args, **kwargs)
        print(f"<<< VERBOSE {func.__qualname__:30} {result=}")
        return result

    return inner


def verbose_methods(cls):
    ignore = ("is_closed", "is_running", "get_debug", "set_debug", "_check_closed", "time", "_call_soon", "_set_coroutine_origin_tracking", "_add_reader", "_remove_reader", "close", "_close", "stop")
    methods = {}
    for name in dir(cls):
        method = getattr(cls, name)
        if (
            not name.startswith("__")
            and callable(method)
            and name not in ignore
        ):
            methods[name] = method
    for name, method in methods.items():
        setattr(cls, name, verbose(method))
    return cls


@verbose_methods
class CustomLoop(type(asyncio.get_event_loop())):
    def _run_once(self):
        # source https://github.com/python/cpython/blob/3.10/Lib/asyncio/base_events.py#L1806
        print(f"RUN ONCE LOOP")
        super()._run_once()


class EventLoopPolicy(BasePolicy):
    """Event loop policy.
    The preferred way to make your application use uvloop:
    >>> import asyncio
    >>> import uvloop
    >>> asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    >>> asyncio.get_event_loop()
    <uvloop.Loop running=False closed=False debug=False>
    """

    def _loop_factory(self):
        return CustomLoop()


async def dummy(name):
    secho(f"dummy start {name=}", fg="red")
    await asyncio.sleep(1)
    secho(f"dummy stop  {name=}", fg="red")


if __name__ == "__main__":
    asyncio.set_event_loop_policy(EventLoopPolicy())
    loop = asyncio.get_event_loop()
    loop.set_task_factory(task_factory)
    # inspect(loop, all=True)
    task1 = loop.run_until_complete(dummy("dummy1"))
    loop.close()
