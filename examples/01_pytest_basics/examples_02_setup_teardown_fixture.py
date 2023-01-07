import pytest
from netmiko import Netmiko


def send_show_command(device, command):
    with Netmiko(**device) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
    return result


@pytest.fixture()
def r1_test_connection():
    params = dict(
        host="192.168.100.1",
        username="cisco",
        password="cisco",
        secret="cisco",
        device_type="cisco_ios",
    )
    r1 = Netmiko(**params)
    r1.enable()
    yield r1
    r1.disconnect()


def test_send_show_command(r1_test_connection):
    params = dict(
        host="192.168.100.1",
        username="cisco",
        password="cisco",
        secret="cisco",
        device_type="cisco_ios",
    )
    cmd = "sh run | i hostname"
    # cmd = "sh clock"
    output = send_show_command(params, cmd)
    correct_output = r1_test_connection.send_command(cmd)
    assert output == correct_output


