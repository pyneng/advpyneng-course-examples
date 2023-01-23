import re
from pprint import pprint
import yaml


def parse_sh_cdp_neighbors(command_output: str) -> list[tuple[str, ...]]:
    regex = re.compile(
        r"(?P<r_dev>\S+) +(?P<l_intf>\S+ \S+)"
        r" +\d+ +[\w ]+ +\S+ +(?P<r_intf>\S+ \S+)"
    )
    connect_list = []
    match_l_dev = re.search(r"(\S+)[>#]", command_output)
    l_dev = match_l_dev.group(1)
    for match in regex.finditer(command_output):
        neighbor = (l_dev, *match.group("l_intf", "r_dev", "r_intf"))
        connect_list.append(neighbor)
    return connect_list


if __name__ == "__main__":
    with open("output/sh_cdp_n_sw1.txt") as f:
        output = f.read()
    pprint(parse_sh_cdp_neighbors(output))
