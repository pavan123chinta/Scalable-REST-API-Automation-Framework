import pytest
from core.base_client import BaseClient


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        help="Environment to run tests against (dev/qa/staging)"
    )


@pytest.fixture(scope="session")
def api_client(request):
    env = request.config.getoption("--env")
    return BaseClient(env)