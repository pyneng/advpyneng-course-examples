import pytest
import subprocess


def ping_ip(ip):
    result = subprocess.run(["ping", "-c", "3", ip], capture_output=True)
    if result.returncode == 0:
        return True
    else:
        return False


@pytest.mark.parametrize("ip_address", ["192.168.100.1", "192.168.100.2", "10.1.1.1"])
def test_ping(ip_address):
    assert ping_ip(ip_address) == True, f"IP {ip_address} должен пинговаться"


def test_loopback(ssh_connection):
    loopback = "Loopback0"
    output = ssh_connection.send_command("sh ip int br")
    assert loopback in output


@pytest.mark.parametrize(
    "command, check_output",
    [("sh ip ospf", "routing process"), ("sh ip int br", "up")],
    ids=["ospf", "interfaces"]
)
def test_services(ssh_connection, command, check_output):
    output = ssh_connection.send_command(command)
    assert check_output in output.lower()
