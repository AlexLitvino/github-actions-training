import random
import requests

url = 'https://gorest.co.in/public/v2/users'


def test_create_user(headers_with_authorization):
    print(headers_with_authorization)
    email = f"anna.ivanova{random.randint(1, 10000000000000)}@test.com"
    user_data = {"name": "Anna Ivanova", "gender": "female", "email": email, "status": "active"}
    response_post = requests.post(url, json=user_data, headers=headers_with_authorization)
    assert response_post.status_code == 201
    user_id = response_post.json()['id']
    get_user_url = f"{url}?id={user_id}"
    response_get = requests.get(get_user_url, headers=headers_with_authorization)
    assert response_get.json()[0]['email'] == email
