import pytest
from basics_01_check_ip import check_ip


@pytest.fixture(params=["10.1.1.1", "180.1.1.1", "240.1.1.30"])
def ip_addr_correct(request):
    return request.param


def test_check_ip_correct(ip_addr_correct):
    assert (
        check_ip(ip_addr_correct) == True
    ), "При правильном IP, функция должна возвращать True"


@pytest.mark.parametrize("ip_address", ["10.1.1", "10.500.1.1", "10.400", "a.a.a.a"])
def test_check_ip_wrong(ip_address):
    assert (
        check_ip(ip_address) == False
    ), "При неправильном IP, функция должна возвращать False"

