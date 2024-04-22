from src.providers.data.repositories_provider import ReposiroriesProvider


def test_check_repos_can_be_found(github_api_client):
    repo = ReposiroriesProvider.existing_repository()
    repos = github_api_client.get_repos(repo['name'])

    assert repos['total_count'] >= repo['total_count']


def test_check_repos_cannot_be_found(github_api_client):
    repo = ReposiroriesProvider.non_existing_repositoryexisting_repository()
    repos = github_api_client.get_repos(repo['name'])
    assert repos['total_count'] == repo['total_count']
    assert len(repos['item']) == repo['total_count']
