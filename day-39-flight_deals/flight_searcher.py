import os
import requests
from datetime import datetime, timedelta


class FlightSearch:

    def __init__(self, hometown: str):
        self.tequila_search_endpoint = "https://tequila-api.kiwi.com/v2/search"
        self.tequila_location_endpoint = "https://tequila-api.kiwi.com/locations/query"
        self.apikey = os.environ["TEQUILA_APIKEY"]
        self.kiwi_header = {"apikey" : self.apikey}
        self.hometown = self.get_IATA(hometown)

    def get_IATA(self, city: str):
        parameters = {"term": city}
        kiwi_response = requests.get(url=self.tequila_location_endpoint, headers=self.kiwi_header, params=parameters)
        return kiwi_response.json()['locations'][0]['code']

    def find_flight(self,
                    destination_city: str,
                    target_price: float,
                    from_time: datetime,
                    to_time: datetime,
                    ):
        parameters = {
            "fly_from": self.hometown,
            "fly_to": destination_city,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "max_stopovers": 0,
            "curr": "EUR",
            }
        kiwi_response = requests.get(url=self.tequila_search_endpoint, headers=self.kiwi_header, params=parameters)
        try:
            kiwi_response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city}.")
            return None

        for flight in kiwi_response.json()["data"]:
            if flight['availability']['seats'] is None:
                continue
            if flight["price"] > target_price:
                break
            else:
                cityto = flight["cityTo"]
                iatato = flight["flyTo"]
                price= flight["price"]
                cityfrom = flight["cityFrom"]
                datefrom = datetime.strptime(flight['route'][0]['local_departure'],'%Y-%m-%dT%H:%M:%S.000Z')
                dateto = datetime.strptime(flight['route'][1]['local_departure'],'%Y-%m-%dT%H:%M:%S.000Z')

                subject = f"Low flight price alert for {cityto}"
                body = f"Only EUR{price} to fly from {cityfrom}-{self.hometown} to {cityto}-{iatato} from {datefrom} to {dateto}"
                return subject, body

