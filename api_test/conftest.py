import pytest

from api_test.helpers import get_token


def pytest_addoption(parser):
    parser.addoption("--token", action="store", default=None)

@pytest.fixture(scope='session')
def token(request):
    cmd_token = request.config.getoption("--token")
    if cmd_token:
        return cmd_token
    else:
        return get_token()


@pytest.fixture(scope='session')
def headers_with_authorization(token):
    print(token)
    return {"Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": token}
