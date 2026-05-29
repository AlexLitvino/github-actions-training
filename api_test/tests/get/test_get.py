import requests

url = 'https://gorest.co.in/public/v2/users'


def test_get_users_status_code(headers_with_authorization):
    response = requests.get(url, headers=headers_with_authorization)
    assert response.status_code == 200


def test_get_users_not_zero_number(headers_with_authorization):
    response = requests.get(url, headers=headers_with_authorization)
    assert len(response.json()) > 0
