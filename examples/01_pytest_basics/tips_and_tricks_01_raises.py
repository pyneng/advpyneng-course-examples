import ipaddress
import pytest


def check_ip(ip):
    if type(ip) != str:
        # return True
        raise TypeError("Function only works with strings")
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


def test_check_ip_raises_0(): # bad
    try:
        check_ip(100)
    except TypeError:
        assert True
    else:
        pytest.fail("Должно было сгенерироваться исключение")


def test_check_ip_raises_1():
    with pytest.raises(TypeError):
        check_ip(100)


def test_check_ip_raises_2():
    with pytest.raises((TypeError, ValueError)):
        check_ip(100)


def test_check_ip_raises_3():
    with pytest.raises(TypeError) as error:
        check_ip(100)
    assert "strings" in str(error.value)


def test_check_ip_raises_4():
    with pytest.raises(TypeError, match="st.+ngs"):
        check_ip(100)
