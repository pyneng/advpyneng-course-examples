from functools import wraps


def bold(func):
    print("Start bold")

    def inner1(*args, **kwargs):
        print(f"Start bold inner1")
        result = f"<b>{func(*args, **kwargs)}</b>"
        print(f"End   bold inner1")
        return result

    return inner1


def italic(func):
    print("Start italic")

    def inner2(*args, **kwargs):
        print(f"Start italic inner2")
        result = f"<i>{func(*args, **kwargs)}</i>"
        print(f"End   italic inner2")
        return result

    return inner2

