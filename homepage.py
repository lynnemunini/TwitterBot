from selenium.webdriver.common.by import By
import time
from login import LoginPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://twitter.com/')
        time.sleep(5)
        sign_in = self.driver.find_element(By.XPATH, "//a[@data-testid='loginButton']")
        sign_in.click()
        time.sleep(5)
        # sign_in_name = self.driver.find_element(By.XPATH,
        #                                    "//*[@id='react-root']/div/div/div/main/div/div/div/div[1]/div/div[3]/a/div/span/span")
        # sign_in_name.click()
        # time.sleep(5)

    def go_to_login_page(self):
        return LoginPage(self.driver)

