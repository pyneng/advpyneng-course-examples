from pprint import pprint


def my_range(start, stop):
    current = start
    while current < stop:
        yield current
        current += 1


def filter_cfg(filename):
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
