# pytest examples_03_fixture_using_fixture.py -v --setup-show --no-header
from my_code import send_show_command


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
