import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("auto-open-devtools-for-tabs")
chrome_driver_path = "/home/daisy/data/udemy/100DoC/chromedriver"


class InternetSpeedTwitterBot:

    def __init__(self, promised_down=150, promised_up=10):
        self.download_speed = None
        self.upload_speed = None
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=chrome_options)
        self.promised_down = promised_down
        self.promised_up = promised_up

    def get_internet_speed(self, url="https://www.speedtest.net/"):
        self.driver.get(url)
        self.driver.set_window_size(1024, 600)
        self.driver.maximize_window()
        cookie_handler = self.driver.find_element(By.XPATH, '//*[@id="onetrust-pc-btn-handler"]')
        self.driver.implicitly_wait(10)
        cookie_handler.click()
        cookie_handler = self.driver.find_element(By.XPATH, '// *[ @ id = "onetrust-pc-sdk"] / div / div[3] / div[1] '
                                                            '/ button')
        cookie_handler.click()
        start_measuring = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div['
                                                             '3]/div[1]/a/span[4]')
        start_measuring.click()
        self.driver.implicitly_wait(20)
        download_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div['
                                                            '3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div['
                                                            '1]/div/div[2]/span')
        upload_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div['
                                                          '3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div['
                                                          '2]/span')
        while len(upload_speed.text) < 3:
            time.sleep(10)
            download_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div['
                                                                '2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div['
                                                                '1]/div[1]/div/div[2]/span')
            upload_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div['
                                                              '3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div['
                                                              '2]/div/div[2]/span')

        self.upload_speed = float(upload_speed.text)
        self.download_speed = float(download_speed.text)
        print(f"Download speed: {self.download_speed}\nUpload Speed: {self.upload_speed}")

    def tweet_current_internet_speed(self, url="https://twitter.com/"):
        self.driver.get(url)
        self.driver.set_window_size(1024, 600)
        self.driver.maximize_window()
        login = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div[1]/div/div/div/div/div/div/div/div['
                                                   '1]/a/div')
        login.click()
        self.driver.implicitly_wait(10)
        email = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div['
                                                   '2]/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(os.getenv("TWITTER_EMAIL"))
        get_to_password = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div['
                                                             '2]/div[2]/div/div[6]/div')
        get_to_password.click()
        username = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div['
                                                      '2]/div[1]/div/div/div[2]/label/div/div[2]/div/input')
        username.send_keys(os.getenv("TWITTER_USERNAME"))
        get_to_password = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div['
                                                             '2]/div[2]/div[2]/div/div/div/div/div/div')
        get_to_password.click()
        password = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div['
                                                      '2]/div[1]/div/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(os.getenv("TWITTER_PASSWORD"))
        final_login = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div['
                                                         '2]/div[2]/div[2]/div/div/div[1]/div/div/div/div')
        final_login.click()
        
        try:
            refuse_cookies = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div[2]/div[2]')
            refuse_cookies.click()
        except NoSuchElementException:
            pass
        following = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div['
                                                       '2]/main/div/div/div/div/div/div[1]/div[1]/div[2]/nav/div/div['
                                                       '2]/div/div[2]/a/div/div/span')
        following.click()
        tweet_activation = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div['
                                                              '2]/main/div/div/div/div/div/div[3]/div/div[2]/div['
                                                              '1]/div/div/div/div[2]/div['
                                                              '1]/div/div/div/div/div/div/div/div/div/div/label/div['
                                                              '1]/div/div')
        tweet_activation.click()
        tweet_input = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div['
                                                         '2]/main/div/div/div/div/div/div[3]/div/div[2]/div['
                                                         '1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div['
                                                         '2]/div/div/div/div/label/div[1]/div/div/div/div/div/div['
                                                         '2]/div/div/div/div')

        text = f"I checked my current Internet speed.\nDownload {self.download_speed}\nUpload {self.upload_speed}"
        tweet_input.send_keys(text)
        tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div['
                                                          '2]/main/div/div/div/div/div/div[3]/div/div[2]/div['
                                                          '1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        tweet_button.click()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_current_internet_speed()
