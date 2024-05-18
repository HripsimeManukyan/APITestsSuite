import pytest
from api_client.client import delete_post


def test_delete_post():
    response = delete_post(1)
    assert response.status_code == 200
