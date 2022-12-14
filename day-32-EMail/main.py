import datetime as dt
import smtplib
import pandas as pd
import random
import sys

my_email = "daisiduuke@gmail.com"
with open("password.txt") as pfile:
    app_password = pfile.read()

day = dt.datetime.now().day
month = dt.datetime.now().month
friends = pd.read_csv("birthdays.csv")
birthday_kids = friends[((friends.day == day) & (friends.month == month))]
birthday_kids = dict(zip(birthday_kids.name, birthday_kids.email))
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=app_password)
    for bkid, email in birthday_kids.items():
        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as letter:
            letter_text = letter.read().replace("[NAME]", bkid)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=f"{email}",
            msg=f"Subject:Happy Birthday\n\n{letter_text}?")

