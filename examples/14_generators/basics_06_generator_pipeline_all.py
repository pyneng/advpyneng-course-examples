import re
from rich import print as rprint


def read_file(filename, regex):
    with open(filename) as f:
        for index, line in enumerate(f, 1):
            if re.search(regex, line):
                line = line.rstrip()
                yield line.lower()


if __name__ == "__main__":
    lower = read_file("config_r1.txt", "^interface")
    # lower = map(str.lower, filt_i)
    for line in lower:
        print(line)

