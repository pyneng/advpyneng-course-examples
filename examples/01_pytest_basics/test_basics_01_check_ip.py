from basics_01_check_ip import check_ip


# плохой вариант потому что проверка будет до первого невыполненного assert
def test_check_wrong_ip():
    for ip in ["10.1.1", "10.500.1.1", "10.400", "a.a.a.a"]:
        assert check_ip(ip) == False


# плохой вариант потому что проверка будет до первого невыполненного assert
def test_check_ip():
    assert (
        check_ip("10.1.1.1") == True
    ), "При правильном IP, функция должна возвращать True"
    assert (
        check_ip("180.10.1.1") == True
    ), "При правильном IP, функция должна возвращать True"
    assert (
        check_ip("10.400.1.1") == False
    ), "При неправильном IP, функция должна возвращать False"
    assert (
        check_ip("10.1.1") == False
    ), "При неправильном IP, функция должна возвращать False"


# нормальный вариант, но грустный
def test_check_ip_correct_10_1_1_1():
    assert (
        check_ip("10.1.1.1") == True
    ), "При правильном IP, функция должна возвращать True"


def test_check_ip_correct_180_10_1_1():
    assert (
        check_ip("180.10.1.1") == True
    ), "При правильном IP, функция должна возвращать True"


def test_check_ip_wrong_octet():
    assert (
        check_ip("10.400.1.1") == False
    ), "При неправильном IP, функция должна возвращать False"


def test_check_ip_wrong_number_of_octets():
    assert (
        check_ip("10.1.1") == False
    ), "При неправильном IP, функция должна возвращать False"
