import sys
import pytest


@pytest.mark.xfail(reason="should fail")
def test_xfail():
    assert False


@pytest.mark.xfail(reason="always xfail")
def test_xpass():
    assert True
