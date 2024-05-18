import pytest
from api_client.client import create_post


@pytest.fixture
def new_post_data():
    return {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }


def test_post_requests(new_post_data):
    response = create_post(new_post_data)
    assert response.status_code == 201
    post = response.json()
    assert post["title"] == new_post_data["title"]
    assert post["body"] == new_post_data["body"]
    assert post["userId"] == new_post_data["userId"]
    print(post)
