import os
import time
from flat import Flat

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("auto-open-devtools-for-tabs")
chrome_driver_path = "/home/daisy/data/udemy/100DoC/chromedriver"

class DataPusher:

    def __init__(self):

        self.driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=chrome_options)

    def enter_information(self, url, flats: [classmethod(Flat)]):
        self.driver.get(url)
        self.driver.set_window_size(1024, 600)
        self.driver.maximize_window()

        for flat in flats:
            self.address_field = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            self.flat_price_field = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            self.flat_size_field = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea')
            self.link_field = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')

            self.address_field.send_keys(flat.get_address())
            self.flat_price_field.send_keys(flat.get_price())
            self.flat_size_field.send_keys(flat.get_flat_size())
            self.link_field.send_keys(flat.get_href())

            send = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
            send.click()
            reset = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
            reset.click()
