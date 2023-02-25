import logging
from functools import wraps


def log(logger=None, fmt="{asctime} {levelname:10} {name} {message}"):
    if logger is None:
        logging.basicConfig(level=logging.DEBUG, format=fmt, style="{", force=True)
        logger = logging.getLogger()

    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            logger.debug(f"Calling {func.__name__} {args=} {kwargs=}")
            return func(*args, **kwargs)

        return inner

    return decorator


@log()
def f(a, b):
    return a + b


f(1, 2)
f(a=5, b=2)
f(100, 200)
