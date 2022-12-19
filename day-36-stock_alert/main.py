import requests
import pandas as pd
import datetime as dt
import smtplib

COIN = "BTC"
COIN_NAME = "Bitcoin"


def get_price_move():
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
    move = (float(close_price) - float(open_price))/float(open_price)
    return move


def get_news():
    news_api_key = "3fcf57bda23a49f6a34c8ad45f020f42"
    endpoint = "https://newsapi.org/v2/everything"
    news_params = {
        "apiKey": news_api_key,
        "from": dt.datetime.today().strftime("%y-%m-%d"),
        "sortBy": "popularity",
        "q": "Bitcoin",
    }
    news_data = requests.get(endpoint, params=news_params)
    articles = news_data.json()["articles"]
    articles = [a["title"] for a in articles if "Bitcoin" in a["description"]]
    string = "\n".join(articles[:3])
    return string


def send_mail(subject, body):
    my_email = "daisiduuke@gmail.com"
    with open("../password.txt") as pfile:
        app_password = pfile.read()

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=app_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=f"jason-ti@web.de",
            msg=f"Subject:{subject}\n\n{body}")


price_move = get_price_move()
if abs(price_move) > 0.00001:
    headline = f"BTC: {round(price_move*100,1)}%"
    news = get_news()
    print("Sending EMails")
    send_mail(headline, news)
