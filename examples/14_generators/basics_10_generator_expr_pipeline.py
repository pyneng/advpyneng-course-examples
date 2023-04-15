import re
from rich import print as rprint


def is_ignore_line(line, ignore_lines):
    for ignore in ignore_lines:
        if ignore in line:
            return True
    return False


def clean_config(config_filename, ignore_lines_with):
    with open(config_filename) as f:
        for index, line in enumerate(f, 1):
            print("READ", index, line.rstrip())
            if "!" not in line and not is_ignore_line(line, ignore_lines_with):
                yield line.rstrip()


if __name__ == "__main__":
    ignore_lines = ("duplex", "alias exec", "Current configuration", "service")
    i_read = clean_config("config_r1_short.txt", ignore_lines)
    i_filter = (line for line in i_read if re.search("^interface", line))
    i_lower = (line.lower() for line in i_filter)
    for _ in range(3):
        print(">>>", next(i_lower))


