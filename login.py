import time
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password, phone):
        # time.sleep(3)
        user_name = self.driver.find_element(By.CLASS_NAME, "r-30o5oe")
        user_name.send_keys(username)
        # time.sleep(2)
        user_name.send_keys(Keys.ENTER)
        time.sleep(5)
        # phone_number = self.driver.find_element(By.CLASS_NAME, "r-30o5oe")
        # phone_number.send_keys(phone)
        # time.sleep(2)
        # phone_number.send_keys(Keys.ENTER)
        # time.sleep(5)
        my_password = self.driver.find_element(By.XPATH, "//input[@type='password']")
        my_password.send_keys(password)
        # time.sleep(2)
        my_password.send_keys(Keys.ENTER)
        time.sleep(5)

    def tweet(self):


