import pytest
from basics_01_check_ip import check_ip, ping_ip


# @pytest.mark.parametrize("ip_address", ["10.1.1.1", "180.1.1.1", "240.1.1.30"])
# def test_check_ip_correct(ip_address):
#     assert (
#         check_ip(ip_address) == True
#     ), "При правильном IP, функция должна возвращать True"
#
#
# @pytest.mark.parametrize("ip_address", ["10.1.1.1", "180.1.1.1", "240.1.1.30"])
# def test_ping_ip(ip_address):
#     assert (
#         ping_ip(ip_address) == True
#     ), "При правильном IP, функция должна возвращать True"



@pytest.fixture(params=["10.1.1.1", "180.1.1.1", "240.1.1.30"])
def ip_address(request):
    return request.param


def test_check_ip_correct(ip_address):
    assert (
        check_ip(ip_address) == True
    ), "При правильном IP, функция должна возвращать True"


def test_ping_ip(ip_address):
    assert (
        ping_ip(ip_address) == True
    ), "При правильном IP, функция должна возвращать True"

