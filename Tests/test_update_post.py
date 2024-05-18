import pytest
from api_client.client import update_post


@pytest.fixture
def new_update_data():
    return {
        "title": "new foo",
        "body": " new bar",
        "userId": 1
    }


def test_post_requests(new_update_data):
    response = update_post(1, new_update_data)
    assert response.status_code == 200
    post = response.json()
    assert post["title"] == new_update_data["title"]
    assert post["body"] == new_update_data["body"]
    assert post["userId"] == new_update_data["userId"]
    print(post)