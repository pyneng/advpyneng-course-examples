import pytest
from netmiko import Netmiko
import yaml


def read_device_inv(filename):
    with open(filename) as f:
        devices = yaml.safe_load(f)
    return devices

devices = read_device_inv("devices.yaml")


def get_id(device_dict):
    return f"{device_dict.get('device_type')} {device_dict.get('host')}"


@pytest.fixture(params=read_device_inv("devices.yaml"), ids=get_id)
def ssh_connection(request):
    with Netmiko(**request.param) as ssh:
        ssh.enable()
        yield ssh


def test_interfaces(ssh_connection):
    output = ssh_connection.send_command("sh ip int br")
    assert "up" in output


