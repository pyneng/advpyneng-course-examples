from pprint import pprint


a = 10


def f(x, y):
    line = "test"
    print(f"{x=} {y=} {line=}")
    pprint(locals())

f(1, 2)

