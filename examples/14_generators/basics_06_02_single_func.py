import re
from rich import print as rprint


def is_ignore_line(line, ignore_lines):
    for ignore in ignore_lines:
        if ignore in line:
            return True
    return False


def clean_config(config_filename, ignore_lines_with, regex):
    cleaned_lines = []
    with open(config_filename) as f:
        for line in f:
            line = line.rstrip()
            if "!" not in line and not is_ignore_line(line, ignore_lines_with):
                if re.search(regex, line):
                    line = line.rstrip()
                    cleaned_lines.append(line.lower())
    return cleaned_lines


if __name__ == "__main__":
    ignore_lines = ("duplex", "alias exec", "Current configuration", "service")
    lower = clean_config("config_r1.txt", ignore_lines, "^interface")
    for line in lower:
        print(line)

