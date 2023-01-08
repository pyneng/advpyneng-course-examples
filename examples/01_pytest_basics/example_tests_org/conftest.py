import pytest
from netmiko import Netmiko


@pytest.fixture(scope="session")
def r1_params():
    params = dict(
        host="192.168.100.1",
        username="cisco",
        password="cisco",
        secret="cisco",
        device_type="cisco_ios",
    )
    return params


@pytest.fixture(scope="session")
def r1_test_connection(r1_params):
    # setup
    r1 = Netmiko(**r1_params)
    r1.enable()
    yield r1
    # teardown
    r1.disconnect()


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
