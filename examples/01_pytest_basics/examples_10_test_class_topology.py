from class_topology import Topology
import pytest


@pytest.fixture
def topology_with_dup_links():
    topology_with_dup = {
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
    return topology_with_dup


@pytest.fixture
def topology_normalized():
    normalized_topology = {
        ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
        ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
        ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
        ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
        ("R3", "Eth0/1"): ("R4", "Eth0/0"),
        ("R3", "Eth0/2"): ("R5", "Eth0/0"),
    }
    return normalized_topology


@pytest.fixture
def topology_instance(topology_normalized):
    top = Topology(topology_normalized)
    return top


def test_topology_norm(topology_with_dup_links, topology_normalized):
    top = Topology(topology_with_dup_links)
    assert top.topology == topology_normalized


def test_topology_delete_link(topology_normalized):
    top = Topology(topology_normalized)
    original_len = len(top.topology)
    top.delete_link(("R1", "Eth0/0"), ("SW1", "Eth0/1"))
    assert ("R1", "Eth0/0") not in top.topology
    assert len(top.topology) == original_len - 1


def test_topology_delete_link_mirror(topology_normalized):
    top = Topology(topology_normalized)
    original_len = len(top.topology)
    top.delete_link(("SW1", "Eth0/1"), ("R1", "Eth0/0"))
    assert ("R1", "Eth0/0") not in top.topology
    assert len(top.topology) == original_len - 1


def test_topology_delete_link_not_exists(topology_normalized, capsys):
    top = Topology(topology_normalized)
    original_len = len(top.topology)
    top.delete_link(("SW13", "Eth0/1"), ("R1", "Eth0/0"))
    out = capsys.readouterr().out
    assert len(top.topology) == original_len
    assert "соединения нет" in out


def test_topology_add(topology_normalized):
    top1 = Topology(topology_normalized)
    orig_len_1 = len(top1.topology)
    top2 = Topology(
        {("R1", "Eth0/4"): ("R7", "Eth0/0"), ("R1", "Eth0/6"): ("R9", "Eth0/0")}
    )
    orig_len_2 = len(top2.topology)
    new_top = top1 + top2
    assert isinstance(new_top, Topology)
    assert len(new_top.topology) == orig_len_1 + orig_len_2
    assert len(top1.topology) == orig_len_1
    assert len(top2.topology) == orig_len_2
