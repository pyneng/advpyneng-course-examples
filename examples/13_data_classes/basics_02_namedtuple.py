from typing import NamedTuple
from pprint import pprint
from collections import UserDict


class Link(NamedTuple):
    device: str
    port: str


class Topology(UserDict):
    def __str__(self):
        top_str = ""
        for l1, l2 in self.data.items():
            top_str += f"{l1} <--> {l2}\n"
        return top_str


top = {
    Link("R1", "Gi0/0"): Link("SW1", "Gi0/1"),
    Link("R2", "Gi0/0"): Link("SW1", "Gi0/2"),
    Link("R2", "Gi0/1"): Link("SW2", "Gi0/11"),
    Link("R3", "Gi0/0"): Link("SW1", "Gi0/3"),
    Link("R3", "Gi0/1"): Link("R4", "Gi0/0"),
    Link("R3", "Gi0/2"): Link("R5", "Gi0/0"),
}


t1 = Topology(top)
pprint(top)
pprint(t1)
print(t1)
