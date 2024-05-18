import pytest
from api_client.client import get_all_posts, get_post


def test_get_all_posts():
    response = get_all_posts()
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_single_post():
    response = get_post(1)
    assert response.status_code == 200
    post = response.json()
    assert isinstance(post, dict)
    assert post['id'] == 1
