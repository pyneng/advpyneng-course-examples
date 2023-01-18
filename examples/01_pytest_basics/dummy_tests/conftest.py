import time
import pytest


@pytest.fixture
def fixture_1_tuple():
    return (1, 2, 3)


@pytest.fixture
def fixture_2_session():
    start = time.sleep(0.5)
    yield True
    end = time.sleep(0.5)


@pytest.fixture(params=["10.255.1.1", "10.255.1.2", "10.255.1.3"])
def fixture_3_session_params(request):
    start = time.sleep(0.3)
    yield request.param
    end = time.sleep(0.3)
