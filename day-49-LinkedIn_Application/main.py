import selenium.common
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os
from time import sleep
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_driver_path = "/home/daisy/data/udemy/100DoC/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=chrome_options)
URL = "https://www.linkedin.com/jobs/search/?currentJobId=3474893679&f_AL=true&f_E=2&f_I=11%2C144%2C12%2C4%2C84%2C96%2C53&f_JT=F&f_PP=106967730%2C100477049&geoId=101282230&keywords=it%20consulting&location=Deutschland&refresh=true&sortBy=R"
driver.get(URL)
driver.set_window_size(1024, 600)
driver.maximize_window()

login_page = driver.find_element(By.XPATH, '/html/body/div[5]/a[1]')
driver.implicitly_wait(10)
login_page.click()

username = driver.find_element(By.XPATH, '//*[@id="username"]')
username.send_keys(os.getenv("LINKEDIN_EMAIL"))
password = driver.find_element(By.XPATH, '//*[@id="password"]')
password.send_keys(os.getenv("LINKEDIN_PASSWORD"))
login_button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
login_button.click()
sleep(5)
#message_dropdown = driver.find_element(By.XPATH, '//*[@id="msg-overlay"]/div[1]/header/div[2]/button/span/span[1]')
#message_dropdown.click()
#save_button = driver.find_element(By.XPATH, '//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/button/span[1]')
#save_button.click()
company_link = driver.find_element(By.XPATH, '//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[1]/span[1]/span[1]')
company_link = company_link.find_elements(By.CLASS_NAME, "ember-view")[0]
company_id = company_link.get_attribute("id")
breakpoint()

company_link.click()
sleep(2)
follow_button = driver.find_element(By.XPATH, f'//*[@id="{company_id}"]/div[2]/div[1]/div[3]/div[1]/div[1]/button')
follow_button.click()
#company_link.click()

