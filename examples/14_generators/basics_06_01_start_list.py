import re
from pprint import pprint


def is_ignore_line(line, ignore_lines):
    for ignore in ignore_lines:
        if ignore in line:
            return True
    return False


def clean_config(config_filename, ignore_lines_with):
    cleaned_lines = []
    with open(config_filename) as f:
        for line in f:
            if "!" not in line and not is_ignore_line(line, ignore_lines_with):
                cleaned_lines.append(line.rstrip())
    return cleaned_lines


def filter_lines(iterable, regex):
    filtered_lines = []
    for line in iterable:
        if re.search(regex, line):
            filtered_lines.append(line)
    return filtered_lines


def convert_to_lower(iterable):
    lower_lines = []
    for line in iterable:
        lower_lines.append(line.lower())
    return lower_lines


if __name__ == "__main__":
    ignore_lines = ("duplex", "alias exec", "Current configuration", "service")
    cfg = clean_config("config_r1_short.txt", ignore_lines)
    f_lines = filter_lines(cfg, "^interface|ip address")
    lower = convert_to_lower(f_lines)
    for line in lower:
        print(line)
