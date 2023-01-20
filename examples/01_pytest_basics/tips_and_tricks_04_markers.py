import pytest


# @pytest.mark.skip(reason="no way of currently testing this")
# @pytest.mark.skipif(sys.version_info < (3, 9), reason="requires python3.9 or higher")
# @pytest.mark.xfail(reason="should fail")
# @pytest.mark.parametrize("ip_address", ["10.1.1.1", "180.1.1.1", "240.1.1.30"])


@pytest.mark.ios
def test_1():
    assert True


@pytest.mark.ios
@pytest.mark.cisco
def test_2():
    assert True


@pytest.mark.cisco
def test_3():
    assert True
