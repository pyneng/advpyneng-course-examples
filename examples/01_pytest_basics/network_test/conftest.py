from pprint import pprint

import pytest
from netmiko import Netmiko
import yaml


def read_device_inv(filename):
    with open(filename) as f:
        devices = yaml.safe_load(f)
    return devices


def get_host(device_params_dict):
    return device_params_dict.get("host")


devices = read_device_inv("devices.yaml")


@pytest.fixture(params=read_device_inv("devices.yaml"), ids=get_host, scope="session")
def ssh_connection(request):
    ssh = Netmiko(**request.param)
    ssh.enable()
    yield ssh
    ssh.disconnect()
