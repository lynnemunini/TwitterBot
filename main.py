from bs4 import BeautifulSoup
import requests
import lxml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from homepage import HomePage
import os

URL = "https://bestlifeonline.com/random-fun-facts/"
response = requests.get(URL)
webpage = response.text
soup = BeautifulSoup(webpage, "lxml")
facts = soup.find_all("div", {"class": "title"})

try:
    with open("facts.txt") as facts_file:
        lines = facts_file.read()

except FileNotFoundError:
    for fact in facts:
        my_fact = fact.getText()
        if my_fact == "Filed Under":
            continue
        with open("facts.txt", "a") as file:
            file.write(f"{my_fact}\n")

# To open twitter

s = Service("/home/lynne/Programs/Development/chromedriver")
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(5)
home_page = HomePage(driver)
login_page = home_page.go_to_login_page()
login_page.login(os.environ["USER"], os.environ["PASSWORD"], os.environ["PHONE"])

