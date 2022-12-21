import os

import requests
import pandas as pd
import smtplib

COIN = "BTC"
COIN_NAME = "Bitcoin"
PERCENT_TRIGGER = 1


def get_price_move_in_percent():
    endpoint = "https://www.alphavantage.co/query"
    trade_api_key = "C5OWVV1SMH8JZ23O"
    parameters = {
        "apikey": trade_api_key,
        "symbol": COIN,
        "market": "USD",
        "function": "DIGITAL_CURRENCY_DAILY"
    }
    response = requests.get(endpoint, params=parameters)
    response.raise_for_status()
    data = response.json()["Time Series (Digital Currency Daily)"]
    df = pd.DataFrame.from_dict(data, orient="index")
    open_price, close_price = df[["1a. open (USD)", "4a. close (USD)"]].values[1, :]
    move = (float(close_price) - float(open_price)) / float(open_price)
    return move*100


def get_news():
    news_api_key = "3fcf57bda23a49f6a34c8ad45f020f42"
    endpoint = "https://newsapi.org/v2/everything"
    news_params = {
        "apiKey": news_api_key,
        # "from": dt.datetime.today().strftime("%y-%m-%d"),
        "sortBy": "popularity",
        "qinTitle": COIN_NAME,
    }
    news_data = requests.get(endpoint, params=news_params)
    articles = news_data.json()["articles"]
    string = "\n".join([a["title"] for a in articles][:3])
    return string


def send_mail(subject, body):
    body = body.encode('ascii', 'ignore').decode('ascii')
    my_email = "daisiduuke@gmail.com"
    app_password = os.getenv("DAISI_PASSWORD")
    print(app_password)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=app_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=f"jason-ti@web.de",
            msg=f"Subject:{subject}\n\n{body}")


price_move_in_percent = get_price_move_in_percent()
if abs(price_move_in_percent) > PERCENT_TRIGGER:
    print("Sending EMails")
    headline = f"{COIN}: {round(price_move_in_percent, 1)}%"
    news = get_news()
    send_mail(headline, news)
