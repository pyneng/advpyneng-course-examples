

def delete_dupl(topology_dict):
    pass


class Topology:
    def __init__(self, topology):
        pass

topology = {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
            ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
            ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
            ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
            ('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
            ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
            ('SW1', 'Eth0/3'): ('R3', 'Eth0/0')}
normalized_topology = {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
                       ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
                       ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
                       ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),

def test_delete_dupl():
    assert delete_dupl(topology) == normalized_topology


def test_topology_class():
    top = Topology(topology)
    assert top.topology == normalized_topology

