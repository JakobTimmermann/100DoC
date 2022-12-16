import smtplib
import requests
import datetime as dt
import time

MY_LAT = 15.583820
MY_LNG = 73.741661

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

my_email = "daisiduuke@gmail.com"
with open("../password.txt") as pfile:
    app_password = pfile.read()


def is_nighttime():
    daylight = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    data = daylight.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    now = dt.datetime.utcnow()
    is_night = sunrise > now.hour > sunset
    if is_night:
        print("Yes! It's nighttime")
    return is_night


def is_in_eyesight():
    space_shuttle = requests.get("http://api.open-notify.org/iss-now.json").json()["iss_position"]
    lat = float(space_shuttle["latitude"])
    lng = float(space_shuttle["longitude"])
    is_above = (MY_LAT+5 > lat > MY_LAT-5) and (MY_LNG+5 > lng > MY_LNG)
    if is_above:
        print("Space Shuttle above!")
    return is_above


while True:
    time.sleep(60)
    if is_in_eyesight() and is_nighttime():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=app_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=f"jason-ti@web.de",
                msg=f"Subject:ISS above\n\nLook up! The ISS should be within eyesight.")

