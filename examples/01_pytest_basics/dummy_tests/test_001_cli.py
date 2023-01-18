import pytest


def test_func_1(fixture_1_tuple):
    assert 1 in fixture_1_tuple


@pytest.mark.parametrize("ip", ["10.1.1.1", "10.2.2.2", "10.1.1.3"])
def test_ping_ip_success(ip):
    assert ip


@pytest.mark.parametrize("ip", ["10.1.1.1", "10.2.2.2", "10.1.1.3"])
def test_ping_ip_failed(ip):
    assert ip == "8.8.8.8"


def test_connection_1(fixture_2_session):
    assert fixture_2_session == True


def test_connection_2(fixture_2_session):
    assert fixture_2_session == True


def test_connection_3(fixture_3_session_params):
    assert "10" in fixture_3_session_params
