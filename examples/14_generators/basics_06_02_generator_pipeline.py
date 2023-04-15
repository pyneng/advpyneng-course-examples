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
            line = line.rstrip()
            print("READ", index, line)
            if "!" not in line and not is_ignore_line(line, ignore_lines_with):
                yield line.rstrip()


def filter_lines(iterable, regex):
    for line in iterable:
        if re.search(regex, line):
            rprint(f"[green]FILTER {line}")
            yield line


def convert_to_lower(iterable):
    for line in iterable:
        rprint(f"[violet]LOWER {line}")
        yield line.lower()


if __name__ == "__main__":
    ignore_lines = ("duplex", "alias exec", "Current configuration", "service")
    file_i = clean_config("config_r1_short.txt", ignore_lines)
    filt_i = filter_lines(file_i, "^interface")
    lower = convert_to_lower(filt_i)
    # lower = map(str.lower, filt_i)
    for line in lower:
        print(line)

    lower = convert_to_lower(
        filter_lines(clean_config("config_r1_short.txt", ignore_lines), "^interface")
    )
    # lower = map(str.lower, filt_i)
    for line in lower:
        print(line)
