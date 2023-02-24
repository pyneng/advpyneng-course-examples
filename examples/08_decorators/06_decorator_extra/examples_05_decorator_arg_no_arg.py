import logging
from functools import wraps


def log(function=None, *, logger=None, fmt="{asctime} {levelname:10} {name} {message}"):
    if logger is None:
        logging.basicConfig(level=logging.DEBUG, format=fmt, style="{", force=True)
        logger = logging.getLogger()

    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            logger.debug(f"Calling {func.__name__} {args=} {kwargs=}")
            return func(*args, **kwargs)

        return inner

    if function is None:
        return decorator
    else:
        return decorator(function)


root = logging.getLogger()
root.setLevel(logging.DEBUG)

stderr = logging.StreamHandler()
stderr.setLevel(logging.DEBUG)
stderr.setFormatter(logging.Formatter("{name} {levelname} {message}", style="{"))

root.addHandler(stderr)


@log(logger=root)
def f(a, b):
    return a + b


f(1, 2)
f(a=5, b=2)
f(100, 200)
