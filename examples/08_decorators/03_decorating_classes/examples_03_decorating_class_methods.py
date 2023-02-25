from functools import wraps


def verbose(func):
    print(f"verbose {func=}")

    @wraps(func)
    def inner(*args, **kwargs):
        print(f"{func.__name__} {args[1:]=} {kwargs=}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} {result=}")
        return result

    return inner


class IPAddress:
    def __init__(self, ip, mask):
        self.ip = ip
        self.mask = mask

    def __repr__(self):
        return f"IPAddress({self.ip}/{self.mask})"

    def bin_mask(self):
        return "1" * self.mask + "0" * (32 - self.mask)
