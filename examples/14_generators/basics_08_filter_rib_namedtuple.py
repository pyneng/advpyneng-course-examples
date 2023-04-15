import csv
from pprint import pprint
from collections import namedtuple
from rich import print as rprint

# "status","network","netmask","nexthop","metric","locprf","weight","path","origin"
# "*","1.0.0.0","24","200.219.145.45",NA,NA,0,"28135 18881 3549 15169","i"
# "*>","1.0.0.0","24","200.219.145.23",NA,NA,0,"53242 7738 15169","i"
# "*","1.0.4.0","24","200.219.145.45",NA,NA,0,"28135 18881 3549 1299 7545 56203","i"
# "*>","1.0.4.0","24","200.219.145.23",NA,NA,0,"53242 12956 174 7545 56203","i"

Route = namedtuple(
    "Route",
    "status network netmask nexthop metric locprf weight path origin"
)


def create_route(iterable):
    for row in iterable:
        yield Route(*row)


def read_rib(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        header = next(reader)
        for index, row in enumerate(reader, 1):
            print("READ", index, row)
            yield row


def filter_by_nhop(iterable, nhop):
    for prefix in iterable:
        if prefix.nexthop == nhop:
            yield prefix


def filter_by_mask(iterable, mask):
    for prefix in iterable:
        if prefix.netmask == mask:
            yield prefix


if __name__ == "__main__":
    f = read_rib("rib_table.csv")
    routes = create_route(f)
    filter_prefix = filter_by_nhop(routes, "200.219.145.23")
    f_mask = filter_by_mask(filter_prefix, "22")

    for _ in range(4):
        line = next(f_mask)
        rprint(f"[violet]>>> {line}")
