import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
import smtplib
import os
viaSoup = True

my_email = "daisiduuke@gmail.com"
app_password = os.getenv("DAISI_PASSWORD")

target_price = 500.00
URL = "https://www.amazon.de/Lenovo-Prozessor-Arbeitsspeicher-1920x1080-General%C3%BCberholt/dp/B099ZWFYLV/ref=sr_1_2?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=lenovo+thinkpad+x1+carbon&qid=1674610009&refinements=p_36%3A-120000&rnid=9708297031&s=computers&sr=1-2"

if viaSoup:
    header = {
        "Accept-Language": "en-US,en;q=0.5",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0"
    }
    response = requests.get(URL,headers=header)
    page = response.text
    soup = BeautifulSoup(page, "html.parser")
    product_title = soup.find(name="span", id="productTitle").text
    product_title = " ".join(product_title.split()[:8])
    price = soup.find(name="span", class_="apexPriceToPay").text

if not viaSoup:
    chrome_driver_path  = "/home/daisy/data/udemy/100DoC/chromedriver"
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    driver.get(URL)
    price = driver.find_element(By.XPATH, '//*[@id="corePrice_desktop"]/div/table/tbody/tr[2]/td[2]/span[1]/span[2]')
    price = price.text

price = float(price.split("€")[1])

if price < target_price:
    body = f"The price for {product_title} is now {price}€ (below target price of {target_price}€)!"
    msg = MIMEText(body, _charset="utf-8")
    msg["Subject"] = "Amazon Price Tracker Alert"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=app_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="jason-ti@web.de",
            msg=msg.as_string()
        )




