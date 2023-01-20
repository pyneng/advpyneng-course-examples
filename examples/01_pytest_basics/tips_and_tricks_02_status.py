import sys
import pytest


if not sys.platform.startswith("win"):
    pytest.skip("skipping windows-only tests", allow_module_level=True)


@pytest.fixture
def error_fixture():
    raise ValueError


def test_ok():
    assert True


def test_fail():
    assert False


def test_error(error_fixture):
    pass


def test_skip():
    pytest.skip("skipping this test")


@pytest.mark.skip(reason="no way of currently testing this")
def test_skip_marker():
    pass


@pytest.mark.skipif(sys.version_info < (3, 9), reason="requires python3.9 or higher")
def test_skipif_marker():
    pass
