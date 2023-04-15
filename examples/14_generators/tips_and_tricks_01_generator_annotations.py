from pprint import pprint
from collections.abc import Iterator, Generator
# Generator[YieldType, SendType, ReturnType]


# def my_range(start: int, stop: int) -> Generator[int, None, None]:
def my_range(start: int, stop: int) -> Iterator[int]:
    current = start
    while current < stop:
        yield current
        current += 1


def filter_cfg(filename: str) -> Iterator[str]:
    with open(filename) as f:
        for line in f:
            if line.startswith("interface"):
                yield line
            elif line.startswith(" switchport"):
                yield line
            elif line.startswith("alias"):
                yield line


for line in filter_cfg("config_sw1.txt"):
    pprint(line)
