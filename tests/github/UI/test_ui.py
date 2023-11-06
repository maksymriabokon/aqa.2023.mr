from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path = "C:\Users\maksym.riabokon\Downloads\chromedriver_win32")
driver.get("https://gihub.com/login")

username_field = driver.find_element_by_id("login_field")

password_field = driver.find_element_by_id("password")

login_button = driver.find_element_by_id("commit")

username_field.send_keys("incorrectLogin")
password_field.send_keys("aaaaaaaaaaaa")
login_button.click()

time.sleep(4)

error_message = driver.find_element_by_css_selector(".flash-error")
assert "Incorrect username or password" in error_message.text
