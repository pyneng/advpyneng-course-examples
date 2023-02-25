from functools import wraps


def d_1(func):
    print("Start decorator 1")

    def inner1(*args, **kwargs):
        print(f"Start inner1 {func.__name__=}")
        print("1" * 40)
        result1 = func(*args, **kwargs)
        print(f"{result1=}")
        print("1" * 40)
        return result1

    return inner1


def d_2(func):
    print("Start decorator 2")

    def inner2(*args, **kwargs):
        print(f"Start inner2 {func.__name__=}")
        print("2" * 40)
        result2 = func(*args, **kwargs)
        print(f"{result2=}")
        print("2" * 40)
        return result2

    return inner2

@d_1
@d_2
def f():
    return 42


# f = d_1(d_2(f))
inner2 = d_2(f)
inner1 = d_1(inner2)
