import pytest


def test_retry_mechanism(api_client):
    with pytest.raises(Exception):
        api_client.get("https://httpstat.us/500")