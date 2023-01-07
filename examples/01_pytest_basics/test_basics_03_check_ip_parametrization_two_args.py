import pytest
from basics_01_check_ip import check_ip


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
)
def test_check_ip(ip_address, result):
    assert (
        check_ip(ip_address) == result
    ), f"При IP = {ip_address}, функция должна возвращать {result}"
