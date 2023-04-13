from pprint import pprint

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

lines = list(filter_cfg("config_sw1.txt"))
pprint(lines)
