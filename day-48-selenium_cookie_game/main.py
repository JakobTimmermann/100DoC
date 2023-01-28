import selenium.common
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "/home/daisy/data/udemy/100DoC/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
URL = "https://orteil.dashnet.org/cookieclicker/"
driver.get(URL)


def get_elements():
    elements = []
    for k in range(8):
        try:
            elements.append(driver.find_element(By.ID, f"upgrade{k}"))
        except selenium.common.exceptions.NoSuchElementException:
            pass
    return elements


language = driver.find_element(By.ID, "langSelect-EN")
language.click()
cookie = driver.find_element(By.ID, "bigCookie")
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]

