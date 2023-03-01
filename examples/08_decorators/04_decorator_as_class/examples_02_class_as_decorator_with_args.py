from functools import wraps, update_wrapper


class Verbose:
    def __init__(self, msg):
        self.msg = msg
        print("init verbose")

    def __call__(self, func):
        print(f"{self.msg} verbose {func=}")

        @wraps(func)
        def inner(*args, **kwargs):
            print(f"__call__ {args=} {kwargs=}")
            result = func(*args, **kwargs)
            print(f"__call__ {result=}")
            return result

        return inner


@Verbose("hello")
def lower(string):
    print(f"lower {string=}")
    return string.lower()


# decorator = Verbose("hello")
# lower = decorator(lower)


def capitalize(string):
    print(f"capitalize {string=}")
    return string.capitalize()
