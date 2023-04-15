import re
from collections.abc import Iterator, Iterable
from rich import print as rprint


def is_ignore_line(line: str, ignore_lines: Iterable[str]) -> bool:
    for ignore in ignore_lines:
        if ignore in line:
            return True
    return False


def clean_config(config_filename: str, ignore_lines_with: Iterable[str]) -> Iterator[str]:
    with open(config_filename) as f:
        for index, line in enumerate(f, 1):
            print("READ", index, line.rstrip())
            if "!" not in line and not is_ignore_line(line, ignore_lines_with):
                yield line.rstrip()


def filter_lines(iterable: Iterable[str], regex: str) -> Iterator[str]:
    for line in iterable:
        if re.search(regex, line):
            rprint(f"[green]FILTER {line}")
            yield line


def convert_to_lower(iterable: Iterable[str]) -> Iterator[str]:
    for line in iterable:
        rprint(f"[violet]LOWER {line}")
        yield line.lower()


if __name__ == "__main__":
    ignore_lines = ("duplex", "alias exec", "Current configuration", "service")
    i_read = clean_config("config_r1_short.txt", ignore_lines)
    i_filter = filter_lines(i_read, "^interface")
    i_lower = convert_to_lower(i_filter)
    # i_lower = map(str.lower, i_filter)
    for _ in range(3):
        print(">>>", next(i_lower))
