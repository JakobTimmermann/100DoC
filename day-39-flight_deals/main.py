import requests
import datetime as dt
import os

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
SHEET_NAME = "cheapFlights"
PROJECT_NAME = "flightDeals"
USER_NAME = os.environ["SHEETY_USERNAME"]
SHEETY_PASSWORD = os.environ["SHEETY_PASSWORD"]

sheety_endpoint = f"https://api.sheety.co/{USER_NAME}/{PROJECT_NAME}/{SHEET_NAME}/2"
print(sheety_endpoint)
sheety_header = {"Authorization": f"Bearer {SHEETY_PASSWORD}"}
sheety_body = {}
sheety_body["cheapflight"] = {"city":"Paris", "code":"asdasd"}
sheet_response = requests.put(url=sheety_endpoint, json=sheety_body, headers=sheety_header)
print(sheet_response.text)

