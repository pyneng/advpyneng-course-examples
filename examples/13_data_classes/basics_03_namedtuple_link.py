from pprint import pprint
from typing import NamedTuple


class Link(NamedTuple):
    device: str
    port: str

    def __str__(self):
        return f"('{self.device}', '{self.port}')"

top = {
    Link("R1", "Gi0/0"): Link("SW1", "Gi0/1"),
    Link("R2", "Gi0/0"): Link("SW1", "Gi0/2"),
    Link("R2", "Gi0/1"): Link("SW2", "Gi0/11"),
    Link("R3", "Gi0/0"): Link("SW1", "Gi0/3"),
    Link("R3", "Gi0/1"): Link("R4", "Gi0/0"),
    Link("R3", "Gi0/2"): Link("R5", "Gi0/0"),
}


pprint(top)
