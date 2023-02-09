from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import os
from time import sleep

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


def initialize_selenium_driver(url):
    """
    Takes in an url pointing to job search results for specific settings
    and sets up and initializes a selenium driver class
    :param url: LinkedIn job search URL
    :return: selenium driver class
    """
    chrome_driver_path = "/home/daisy/data/udemy/100DoC/chromedriver"
    driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=chrome_options)
    driver.get(url)
    driver.set_window_size(1024, 600)
    driver.maximize_window()
    return driver


def login_to_LinkedIn(driver):
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
    message_dropdown = driver.find_element(By.XPATH, '//*[@id="msg-overlay"]/div[1]/header/div[2]/button/span/span[1]')
    message_dropdown.click()


def extract_jobs(driver):
    jobs_segment = driver.find_element(By.XPATH, '//*[@id="main"]/div/section[1]/div/ul')
    jobs = jobs_segment.find_elements(By.CLASS_NAME, "job-card-container__link")
    return jobs


def save_job_if_new(driver, job):
    job.click()
    sleep(5)
    save_button = driver.find_element(By.XPATH, '//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div['
                                                '1]/div[1]/div[3]/div/button/span[1]')
    if save_button.text == "Speichern":
        save_button.click()
        follow_company(driver)
        return False
    return True


def follow_company(driver):
    """
    Extracts company link
    Visits company site
    Follows company if not already a follower
    and goes back to job application page
    """
    company_link = driver.find_element(By.XPATH, '//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div['
                                                 '1]/div/div[1]/div[1]/div[1]/span[1]/span[1]')
    company_link = company_link.find_elements(By.CLASS_NAME, "ember-view")[0]
    company_link.click()
    sleep(5)
    follow_button = driver.find_element(By.CLASS_NAME, "follow")
    if follow_button.text == "Folgen":
        follow_button.click()
        try:
            close_button = driver.find_element(By.CSS_SELECTOR, '[aria-label="Verwerfen"]')
            close_button.click()
        except NoSuchElementException:
            pass
    sleep(2)


jobs_url = "https://www.linkedin.com/jobs/search/?currentJobId=3474893679&f_AL=true&f_E=2&f_I=11%2C144%2C12%2C4%2C84" \
           "%2C96%2C53&f_JT=F&f_PP=106967730%2C100477049&geoId=101282230&keywords=it%20consulting&location" \
           "=Deutschland&refresh=true&sortBy=R"
linkedIn_driver = initialize_selenium_driver(jobs_url)
login_to_LinkedIn(linkedIn_driver)
interesting_jobs = extract_jobs(linkedIn_driver)
for job_idx in range(len(interesting_jobs)):
    interesting_jobs = extract_jobs(linkedIn_driver)
    possible_job = interesting_jobs[job_idx]
    is_new = save_job_if_new(linkedIn_driver, possible_job)
    if is_new:
        linkedIn_driver.get(jobs_url)
        sleep(5)
