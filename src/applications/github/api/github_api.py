import requests


class GitHubAPI:

    def __init__(self, base_url_api: str, version) -> None:
        self.base_url = base_url_api
        self.version = version

    def get_user(self, username: str):
        req = requests.get(f"{self.base_url}/users/{username}")
        req.raise_for_status()

        return req.json()

    def get_repos(self, repos_search_param: str):
        req = requests.get(
            f"{self.base_url}/users/search/repositories", params={'q': repos_search_param})
        req.raise_for_status()
        return req.json()
