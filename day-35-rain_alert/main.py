import requests
import smtplib
import os

my_email = "daisiduuke@gmail.com"
with open("../password.txt") as pfile:
    app_password = pfile.read()

OWM_Endpoint = "http://api.weatherapi.com/v1/forecast.json"
api_key = os.environ.get("OWM_API_KEY")
parameters = {
    "key": api_key,
    "q": "Anjuna",
    "days": "1",
    }

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()["forecast"]["forecastday"]
weather_data = response.json()["forecast"]["forecastday"][0]["hour"][7:18]
weather_string = [hour["condition"]["text"] for hour in weather_data]
print(weather_string)
if "rain" in ''.join(weather_string).lower():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=app_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=f"jason-ti@web.de",
            msg=f"Subject:Bring an umbrella...\n\n...it is going to rain.")

