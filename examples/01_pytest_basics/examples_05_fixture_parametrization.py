import pytest
from netmiko import Netmiko


def send_show_command(device, command):
    with Netmiko(**device) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
    return result

common_params = dict(
    username="cisco",
    password="cisco",
    secret="cisco",
    device_type="cisco_ios",
)
ip_list = ["192.168.100.1", "192.168.100.2", "192.168.100.3"]
test_devices = [{"host": ip, **common_params} for ip in ip_list]


@pytest.fixture(params=test_devices, ids=["r1", "r2", "r3"], scope="session")
def dev_params(request):
    return request.param


def test_send_show_command_sh_intf(dev_params):
    cmd = "sh ip int br"
    output = send_show_command(dev_params, cmd)
    assert dev_params["host"] in output


def test_send_show_command_sh_run(dev_params):
    cmd = "sh run"
    output = send_show_command(dev_params, cmd)
    assert dev_params["host"] in output


@pytest.mark.parametrize("command", ["sh run", "sh ip int br"])
def test_send_show_command(dev_params, command):
    output = send_show_command(dev_params, command)
    assert dev_params["host"] in output

