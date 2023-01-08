import pytest
from basics_03_connect import send_show_command

ip_list = ["192.168.100.1", "192.168.100.2", "192.168.100.3"]
common_params = {
    "device_type": "cisco_ios",
    "password": "cisco",
    "secret": "cisco",
    "username": "cisco",
}
test_devices = [{"host": ip, **common_params} for ip in ip_list]


@pytest.fixture(params=test_devices, ids=ip_list)
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
def test_send_show_command_show(dev_params, command):
    output = send_show_command(dev_params, command)
    assert dev_params["host"] in output
