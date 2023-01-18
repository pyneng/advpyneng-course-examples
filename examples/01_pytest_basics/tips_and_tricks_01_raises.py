import ipaddress
import pytest


def check_ip(ip):
    if type(ip) != str:
        # return True
        raise ValueError(f"'{ip}' does not appear to be an IP address")
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False


@pytest.mark.parametrize("ip_address", ["10.1.1.1", "180.1.1.1", "240.1.1.30"])
def test_check_ip_correct(ip_address):
    assert (
        check_ip(ip_address) == True
    ), "При правильном IP, функция должна возвращать True"


@pytest.mark.parametrize("ip_address", ["10.1.1", "10.500.1.1", "10.400", "a.a.a.a"])
def test_check_ip_wrong(ip_address):
    assert (
        check_ip(ip_address) == False
    ), "При неправильном IP, функция должна возвращать False"


def test_check_ip_wrong_1():
    with pytest.raises((ValueError, TypeError)):
        check_ip(100)


def test_check_ip_wrong_2():
    with pytest.raises(ValueError) as error:
        check_ip(1000)
    assert "does not appear to be an IP address" in str(error.value)


def test_check_ip_wrong_3():
    with pytest.raises(ValueError, match="does not appear .+ IP address") as error:
        check_ip(1000)

