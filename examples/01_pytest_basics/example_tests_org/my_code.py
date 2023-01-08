from netmiko import Netmiko


def delete_dupl(topology_dict):
    """DUMMY"""
    return {
        ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
        ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
        ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
        ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
        ("R3", "Eth0/1"): ("R4", "Eth0/0"),
        ("R3", "Eth0/2"): ("R5", "Eth0/0"),
    }


class Topology:
    """DUMMY"""

    def __init__(self, topology):
        self.topology = {
            ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
            ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
            ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
            ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
            ("R3", "Eth0/1"): ("R4", "Eth0/0"),
            ("R3", "Eth0/2"): ("R5", "Eth0/0"),
        }


def send_show_command(device, command):
    with Netmiko(**device) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
    return result
