from class_ipaddress import IPAddress
import pytest


@pytest.fixture
def ipaddress_instance():
    pass


def test_ipaddress_attributes():
    """Проверяем значения атрибутов"""
    ip = IPAddress("10.1.1.1", 25)
    assert ip.ip == "10.1.1.1"
    assert ip.mask == 25


def test_ipaddress_str_repr():
    """Проверяем работу __str__, __repr__"""
    ip = IPAddress("10.1.1.1", 25)
    assert str(ip) == "10.1.1.1/25"
    assert repr(ip) == "IPAddress('10.1.1.1', 25)"


def test_ipaddress_int():
    """Проверяем значения атрибутов"""
    ip = IPAddress("10.1.1.1", 25)
    assert int(ip) == 167837953


def test_ipaddress_cmp_basic():
    """Проверяем значения атрибутов"""
    ip1 = IPAddress("10.2.1.1", 25)
    ip2 = IPAddress("10.10.1.1", 25)
    assert ip1 < ip2
    assert ip1 != ip2
    assert ip1 <= ip2


def test_ipaddress_cmp_ip_mask():
    """Проверяем значения атрибутов"""
    ip1 = IPAddress("10.10.1.1", 24)
    ip2 = IPAddress("10.10.1.1", 25)
    assert ip1 < ip2
    assert ip1 != ip2
    assert ip1 <= ip2


def test_ipaddress_cmp_equal():
    """Проверяем значения атрибутов"""
    ip1 = IPAddress("10.10.1.1", 24)
    ip2 = IPAddress("10.10.1.1", 24)
    assert ip1 == ip2
    assert ip1 <= ip2


def test_ipaddress_cmp_raise():
    """Проверяем значения атрибутов"""
    ip1 = IPAddress("10.10.1.1", 24)
    ip2 = 100
    with pytest.raises(TypeError):
        ip1 < ip2
