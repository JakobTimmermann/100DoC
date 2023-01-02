import requests
import os
import pandas as pd


class DataManager:

    def __init__(self, sheety_endpoint, sheety_header):
        self.sheety_endpoint = sheety_endpoint
        self.sheety_header = sheety_header
        sheet_response = requests.get(url=self.sheety_endpoint, headers=self.sheety_header)
        self.sheet_data = pd.DataFrame(sheet_response.json()["cheapFlights"])

    def update_IATA(self, idx: int, iata: str):
        sheety_body = {"cheapflight": {"city": "Paris", "code": iata}}
        sheet_response = requests.put(
            url=self.sheety_endpoint,
            json=sheety_body,
            headers=self.sheety_header,
            )
        print(sheet_response.text)


