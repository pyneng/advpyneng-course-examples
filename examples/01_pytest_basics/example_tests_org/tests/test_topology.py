from my_code import Topology, delete_dupl


def test_delete_dupl(topology_with_dupl_links, normalized_topology_example):
    assert delete_dupl(topology_with_dupl_links) == normalized_topology_example


def test_topology_class(topology_with_dupl_links, normalized_topology_example):
    top = Topology(topology_with_dupl_links)
    assert top.topology == normalized_topology_example
