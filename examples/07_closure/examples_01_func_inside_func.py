import io
from pprint import pprint


def parse_file(filename):
    def get_lines(open_file):
        lines = [line.strip() for line in open_file if line.strip()]
        return line

    if isinstance(filename, str):
        with open(filename) as f:
            return get_lines(f)
    elif isinstance(filename, io.TextIOBase):
        return get_lines(filename)
    else:
        raise TypeError



if __name__ == "__main__":
    pprint(parse_file("sh_ip_int_br.txt"))
    with open("sh_ip_int_br.txt") as f:
        pprint(parse_file(f))
