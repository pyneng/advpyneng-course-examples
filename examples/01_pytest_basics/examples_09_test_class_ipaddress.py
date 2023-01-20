from class_ipaddress import IPAddress
import pytest


def test_ipaddress_attrs():
    ip1 = IPAddress("10.1.1.1", 25)
    assert ip1.ip == "10.1.1.1"
    assert ip1.mask == 25


def test_ipaddress_str_repr():
    ip1 = IPAddress("10.1.1.1", 25)
    assert str(ip1) == "10.1.1.1/25"
    assert repr(ip1) == "IPAddress('10.1.1.1', 25)"


def test_ipaddress_int():
    ip1 = IPAddress("10.1.1.1", 25)
    assert int(ip1) == 167837953


def test_ipaddress_cmp_basic():
    ip1 = IPAddress("10.2.1.1", 25)
    ip2 = IPAddress("10.10.1.1", 25)
    assert ip1 < ip2
    assert ip2 > ip1
    assert ip1 != ip2
    assert not ip1 == ip2
    assert ip1 <= ip2
    assert ip2 >= ip1


def test_ipaddress_cmp_mask():
    ip1 = IPAddress("10.2.1.1", 24)
    ip2 = IPAddress("10.2.1.1", 25)
    assert ip1 < ip2
    assert ip2 > ip1
    assert ip1 != ip2
    assert not ip1 == ip2
    assert ip1 <= ip2
    assert ip2 >= ip1


def test_ipaddress_cmp_equal():
    ip1 = IPAddress("10.2.1.1", 24)
    ip2 = IPAddress("10.2.1.1", 24)
    assert ip1 == ip2


def test_ipaddress_cmp_raise():
    ip1 = IPAddress("10.2.1.1", 24)
    ip2 = 100
    with pytest.raises(TypeError):
        ip1 == ip2
    with pytest.raises(TypeError):
        ip1 <= ip2
    with pytest.raises(TypeError):
        ip1 > ip2

