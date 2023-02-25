from functools import wraps, update_wrapper


def verbose(func):
    print(f"verbose {func=}")

    @wraps(func)
    def inner(*args, **kwargs):
        print(f"inner {args=} {kwargs=}")
        result = func(*args, **kwargs)
        print(f"inner {result=}")
        return result

    return inner


class Verbose:
    def __init__(self, func):
        print(f"verbose {func=}")
        update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"__call__ {args=} {kwargs=}")
        result = self.func(*args, **kwargs)
        print(f"__call__ {result=}")
        return result



@Verbose
def lower(string):
    print(f"lower {string=}")
    return string.lower()

# lower = Verbose(lower)


def capitalize(string):
    print(f"capitalize {string=}")
    return string.capitalize()
