import re
from datetime import datetime
import asyncio
from asyncio.tasks import _PyTask
from asyncio.events import BaseDefaultEventLoopPolicy as BasePolicy
from functools import wraps
from rich import print as rprint


def time():
    return datetime.now().strftime("%H:%M:%S")


def verbose_methods_filter(include=None, ignore=None, verbose=lambda f: f):
    if ignore is None:
        ignore = set()
    if include is None:
        include = set()

    def verbose_methods(cls):
        all_attrs = set(dir(cls))
        if include:
            all_attrs = set(include)
        elif ignore:
            all_attrs -= set(ignore)
        methods = {}
        for name in all_attrs:
            method = getattr(cls, name)
            if callable(method) and not re.search(r"__\S+__", name):
                # if callable(method):
                methods[name] = method
        for name, method in methods.items():
            setattr(cls, name, verbose(method))
        return cls

    return verbose_methods

