import requests
import pytest
from src.providers.data.users_provider import UsersProvider


def test_user_exists(github_api_client):

    user = UsersProvider.existing_user()
    api_user = github_api_client.get_user(user['login'])
    assert api_user['login'] == user['login']
    assert api_user['id'] == user['id']


def test_non_exists_user(github_api_client):
    user = UsersProvider.fake_user_user()
    with pytest.raises(requests.exceptions.HTTPError):
        github_api_client.get_user(user['login'])
