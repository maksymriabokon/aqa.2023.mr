from selenium import webdriver
from selenium.webdriver.common.by import By


class GitHubUILoginPage:

    def __init__(self) -> None:
        self.driver = webdriver.Edge()

    def navigate_to_page(self):
        self.driver.get("https://github.com/login")

    def try_to_login(self, username, password):
        username_field = self.driver.find_element(By.ID, 'login_field')
        username_field.send_keys(username)

        password_field = self.driver.find_element(By.ID, 'password')
        password_field.send_keys(password)

        login_button = self.driver.find_element(By.NAME, 'commit')
        login_button.click()

    def check_error_message(self):
        error_message = self.driver.find_element(
            By.CLASS_NAME, 'js-flash-alert')

        return error_message is not None

    def close_browser(self):
        self.driver.quit()
