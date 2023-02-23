from functools import wraps


def kwargs_only(func):
    print(f"kwargs_only {func=}")

    @wraps(func)
    def inner(**kwargs):
        """TEEEST"""
        return func(**kwargs)

    if inner.__doc__ is None:
        inner.__doc__ = ""
    inner.__doc__ += "\nФункция принимает только ключевые аргументы"
    return inner



def kwargs_only2(func):
    print(f"kwargs_only {func=}")

    @wraps(func)
    def inner(*args, **kwargs):
        if args:
            raise TypeError("Функция принимает только ключевые аргументы")
        return func(**kwargs)

    return inner


@kwargs_only
def upper(string):
    """Upper function"""
    print(f"upper {string=}")
    return string.upper()


def lower(string):
    print(f"lower {string=}")
    return string.lower()


def capitalize(string):
    print(f"capitalize {string=}")
    return string.capitalize()


@kwargs_only
def sum(a, b):
    return a + b
