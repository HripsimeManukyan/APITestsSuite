import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_all_posts():
    return requests.get(f"{BASE_URL}/posts")


def get_post(post_id):
    return requests.get(f"{BASE_URL}/posts/{post_id}")


def create_post(post_data):
    return requests.post(f"{BASE_URL}/posts", json=post_data)


def update_post(post_id, post_data):
    return requests.put(f"{BASE_URL}/posts/{post_id}", json=post_data)


def delete_post(post_id):
    return requests.delete(f"{BASE_URL}/posts/{post_id}")
