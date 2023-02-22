from functools import wraps


def verbose(func):
    print(f"verbose {func=}")

    @wraps(func)
    def inner(*args, **kwargs):
        print(f"inner {args=} {kwargs=}")
        result = func(*args, **kwargs)
        print(f"inner {result=}")
        return result

    # inner.__doc__ = func.__doc__
    return inner


@verbose
def upper(string):
    """Upper function"""
    print(f"upper {string=}")
    return string.upper()


# upper = verbose(upper)


def lower(string):
    print(f"lower {string=}")
    return string.lower()


def capitalize(string):
    print(f"capitalize {string=}")
    return string.capitalize()


def sum(a, b):
    return a + b
