from pprint import pprint
import pytest
from basics_01_check_ip import check_ip


def get_id_wrong_ip(ip):
    if ip[0].isdigit():
        return f"WRONG IP {ip}"
    else:
        return None


def get_id(param):
    if param == True:
        return "CORRECT"
    elif param == False:
        return "WRONG"
    else:
        return None


@pytest.mark.parametrize(
    "ip_address",
    ["10.1.1.1", "255.255.255.255", "240.1.1.30"],
    ids=["unicast", "broadcast", "multicast"],
)
def test_check_ip_correct(ip_address):
    assert check_ip(ip_address) == True


@pytest.mark.parametrize(
    "ip_address", ["10.1.1", "10.500.1.1", "10.400", "a.a.a.a"], ids=get_id_wrong_ip
)
def test_check_ip_wrong(ip_address):
    assert check_ip(ip_address) == False


@pytest.mark.parametrize(
    "ip_address, result",
    [
        ("10.1.1.1", True),
        ("180.1.1.1", True),
        ("240.1.1.30", True),
        ("10.1.1", False),
        ("10.500.1.1", False),
        ("10.400", False),
        ("a.a.a.a", False),
    ],
    ids=get_id,
)
def test_check_ip(ip_address, result):
    assert check_ip(ip_address) == result
