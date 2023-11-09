from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pytest
from src.applications.github.ui.github_ui import GitHubUILoginPage


def test_github_login():
    github_login = webdriver.Edge()

    github_login.get("https://github.com/login")

    time.sleep(3)

    username_field = github_login.find_element(By.ID, 'login_field')
    username_field.send_keys("incorrectLogin")

    password_field = github_login.find_element(By.ID, 'password')
    password_field.send_keys("Aaaaaaaaaaaa02")

    time.sleep(3)

    login_button = github_login.find_element(By.NAME, 'commit')
    login_button.click()

    error_message = github_login.find_element(By.CLASS_NAME, 'js-flash-alert')
    time.sleep(6)
    assert error_message is not None


@pytest.fixture
def github_login_page_object():
    github_login = GitHubUILoginPage()
    github_login.navigate_to_page()

    yield github_login

    github_login.close_browser()


def test_github_login_negative_page_object(github_login_page_object):
    github_login_page_object.try_to_login('weergbdgd', 'dfgegertgt45545')

    assert github_login_page_object.check_error_message()
