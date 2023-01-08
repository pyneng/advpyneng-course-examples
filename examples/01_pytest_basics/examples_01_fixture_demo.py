import pytest


def delete_dupl(topology_dict):
    return {
        ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
        ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
        ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
        ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
        ("R3", "Eth0/1"): ("R4", "Eth0/0"),
        ("R3", "Eth0/2"): ("R5", "Eth0/0"),
    }


class Topology:
    def __init__(self, topology):
        self.topology = {
            ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
            ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
            ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
            ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
            ("R3", "Eth0/1"): ("R4", "Eth0/0"),
            ("R3", "Eth0/2"): ("R5", "Eth0/0"),
        }


@pytest.fixture()
def topology_with_dupl_links():
    topology = {
        ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
        ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
        ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
        ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
        ("R3", "Eth0/1"): ("R4", "Eth0/0"),
        ("R3", "Eth0/2"): ("R5", "Eth0/0"),
        ("SW1", "Eth0/1"): ("R1", "Eth0/0"),
        ("SW1", "Eth0/2"): ("R2", "Eth0/0"),
        ("SW1", "Eth0/3"): ("R3", "Eth0/0"),
    }
    return topology


@pytest.fixture()
def normalized_topology_example():
    normalized_topology = {
        ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
        ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
        ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
        ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
        ("R3", "Eth0/1"): ("R4", "Eth0/0"),
        ("R3", "Eth0/2"): ("R5", "Eth0/0"),
    }
    return normalized_topology


def test_delete_dupl(topology_with_dupl_links, normalized_topology_example):
    assert delete_dupl(topology_with_dupl_links) == normalized_topology_example


def test_topology_class(topology_with_dupl_links, normalized_topology_example):
    top = Topology(topology_with_dupl_links)
    assert top.topology == normalized_topology_example
