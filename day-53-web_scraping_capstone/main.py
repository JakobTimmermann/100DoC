from bs4 import BeautifulSoup
import requests
from flat import Flat
from data_pusher import DataPusher

HEADERS = {
    "Accept-Language": "en-US,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0"
}

neukoelln_listings = "https://www.wg-gesucht.de/wohnungen-in-Berlin.8.2.1.0.html?offer_filter=1&city_id=8&sort_column" \
                     "=3&sort_order=0&noDeact=1&dFr=1685613600&dTo=1693476000&categories%5B%5D=2&rent_types%5B%5D=1" \
                     "&sMin=50&rMax=2000&dFrDe=31&dToDe=31&ot%5B%5D=165&radDis=1000"

google_form_URL = "https://docs.google.com/forms/d/e/1FAIpQLSewDWwp44C2V1PylEZsIxru1isfj4Nh2Fzn6Q3lLfonlG5A-w" \
                  "/viewform?usp=sf_link"


def flat_finder(wg_gesucht_url):

    response = requests.post(wg_gesucht_url, headers=HEADERS)
    page = response.text
    soup = BeautifulSoup(page, "html.parser")
    flat_listings = []
    all_flats_data = soup.find_all(name="div", class_="offer_list_item")
    for flat_data in all_flats_data:
        flat_listings.append(Flat(flat_data))
    return flat_listings


available_flats = flat_finder(neukoelln_listings)
bot = DataPusher()
bot.enter_information(url=google_form_URL, flats=available_flats)

