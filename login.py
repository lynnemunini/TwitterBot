import time
import random
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import datetime as dt
now_time = dt.datetime.now()


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

        new_tweet = self.driver.find_element(By.CLASS_NAME, "public-DraftStyleDefault-block")
        # Tweet
        with open("facts.txt") as facts_file:
            lines = facts_file.readlines()
            random_fact = random.choices(lines)
            fact = random_fact[0].strip()
            new_tweet.send_keys(fact)
            time.sleep(3)
            tweet_button = self.driver.find_element(By.XPATH, "//div[@data-testid='tweetButtonInline']")
            tweet_button.click()
            time.sleep(5)








