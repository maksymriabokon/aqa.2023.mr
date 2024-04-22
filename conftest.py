from src.config.config_easy import Config
from src.applications.github.api.github_api import GitHubAPI
import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from src.applications.github.ui.github_ui import GitHubUILoginPage


@pytest.fixture(scope='session')
def github_api_client():
    github_api_client = GitHubAPI(Config.base_url_api, 'v1')

    yield github_api_client
    print('end-up test')


@pytest.fixture(scope='session')
def github_ui_client():
    service_object = Service()
    driver = webdriver.Chrome(service=service_object)

    github_ui_client = GitHubUILoginPage(Config.base_url_ui, driver)

    yield github_ui_client

    github_ui_client.close_browser()
