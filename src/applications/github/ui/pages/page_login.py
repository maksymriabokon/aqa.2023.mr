from selenium.webdriver.common.by import By


class PageLogin:
    def __init__(self, driver, base_url) -> None:
        self.driver = driver
        self.login_url = base_url + '/login'

    def navigate(self):
        self.driver.get(self.login_url)
# fields section

    @property
    def login_field(self):
        return self.driver.find_element(By.ID, 'login_field')

    @property
    def pass_field(self):
        return self.driver.find_element(By.ID, 'password')

    @property
    def login_button(self):
        return self.driver.find_element(By.NAME, 'commit')

    @property
    def sign_up_link(self):
        return self.driver.find_element(By.LINK_TEXT, 'Create an account')
# business methods

    def login(self, username, password):
        self.navigate()

        self.login_field.send_keys(username)
        self.pass_field.send_keys(password)

        self.login_button.click()

        if self.is_login_error():
            return True
        return False

    def proceed_to_signup_page(self):
        self.sign_up_link.click()
        return True
# validation checks

    def is_login_error(self):
        return self.driver.title != "Sign in to GitHub"
