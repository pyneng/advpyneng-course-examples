

def parse_file(filename):
    def get_clean_lines(open_file):
        lines = [line.strip() for line in open_file if line.strip()]
        return lines

    if isinstance(filename, str):
        with open(filename) as f:
            return get_clean_lines(f)
    else:
        return get_clean_lines(f)
