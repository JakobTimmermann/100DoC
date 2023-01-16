import requests
import os
import pandas as pd

SHEET_NAME = "cheapFlights"
PROJECT_NAME = "flightDeals"
USER_NAME = os.environ["SHEETY_USERNAME"]
SHEETY_PASSWORD = os.environ["SHEETY_PASSWORD"]


class DataManager:

    def __init__(self):
        self.sheety_endpoint= f"https://api.sheety.co/{USER_NAME}/{PROJECT_NAME}/{SHEET_NAME}"
        self.sheety_header = {"Authorization": f"Bearer {SHEETY_PASSWORD}"}
        sheet_response = requests.get(url=self.sheety_endpoint, headers=self.sheety_header)
        self.sheet_data = pd.DataFrame(sheet_response.json()["cheapFlights"])

    def update_IATA(self, idx: int, iata: str):
        sheety_body = {"cheapflight": {"iataCode": iata}}
        sheet_response = requests.put(
            url=self.sheety_endpoint + f"/{idx+2}",
            json=sheety_body,
            headers=self.sheety_header,
            )


