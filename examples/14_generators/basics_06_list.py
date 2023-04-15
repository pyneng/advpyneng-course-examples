import re
from rich import print as rprint


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
    file_i = clean_config("config_r1.txt", ignore_lines)
    filt_i = filter_lines(file_i, "^interface")
    lower = convert_to_lower(filt_i)
    for line in lower:
        print(line)

