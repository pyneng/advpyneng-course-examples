# pytest examples_03_fixture_using_fixture.py -v --setup-show --no-header
import pytest
from netmiko import Netmiko


def send_show_command(device, command):
    with Netmiko(**device) as ssh:
        ssh.enable()
        result = ssh.send_command(command)
    return result


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


def test_send_show(r1_test_connection, r1_params):
    cmd = "sh run | i hostname"
    output = send_show_command(r1_params, cmd)
    correct_output = r1_test_connection.send_command(cmd)
    # r1_params["password"] = "1231398714895"
    assert output == correct_output


def test_send_show_command(r1_test_connection, r1_params):
    cmd = "sh run | i hostname"
    output = send_show_command(r1_params, cmd)
    correct_output = r1_test_connection.send_command(cmd)
    assert output == correct_output


def test_send_show_command_intf(r1_test_connection, r1_params):
    cmd = "sh run | i interface"
    output = send_show_command(r1_params, cmd)
    correct_output = r1_test_connection.send_command(cmd)
    assert output == correct_output


def test_send_show_command_sh_intf(r1_params):
    cmd = "sh ip int br"
    output = send_show_command(r1_params, cmd)
    assert r1_params["host"] in output
