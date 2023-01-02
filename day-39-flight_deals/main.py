import requests
import datetime as dt
import os
from flight_searcher import FlightSearch
from data_manager import DataManager
import pandas as pd

SHEET_NAME = "cheapFlights"
PROJECT_NAME = "flightDeals"
USER_NAME = os.environ["SHEETY_USERNAME"]
SHEETY_PASSWORD = os.environ["SHEETY_PASSWORD"]
sheety_endpoint= f"https://api.sheety.co/{USER_NAME}/{PROJECT_NAME}/{SHEET_NAME}"
sheety_header = {"Authorization": f"Bearer {SHEETY_PASSWORD}"}

TodaysFlightSearch = FlightSearch()
TodaysDataManager = DataManager(sheety_endpoint, sheety_header)
sheet_data = TodaysDataManager.sheet_data
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"

for idx, row in sheet_data[sheet_data.iataCode == ''].iterrows():
    iataCode = TodaysFlightSearch.get_IATA(row["city"])
    print(idx, iataCode)
#    TodaysDataManager.update_IATA(idx, iataCode)
    sheety_body = {"cheapflight": {"iataCode": iataCode}}
    print(sheety_endpoint + f"/{idx+2}")
    sheet_response = requests.put(
       url=sheety_endpoint + f"/{idx+2}",
       json=sheety_body,
       headers=sheety_header,
       )
    print(sheet_response.text)