from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def test_github_login():
    driver = webdriver.Edge()

    driver.get("https://github.com/login")

    time.sleep(3)

    username_field = driver.find_element(By.ID, 'login_field')
    username_field.send_keys("incorrectLogin")

    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys("Aaaaaaaaaaaa02")

    time.sleep(3)

    login_button = driver.find_element(By.NAME, 'commit')
    login_button.click()

    error_message = driver.find_element(By.CLASS_NAME, 'js-flash-alert')
    time.sleep(6)
    assert error_message is not None
