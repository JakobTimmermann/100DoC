import requests
import datetime as dt

today = dt.datetime.today()

USERNAME = "daisyduke"
with open("../password.txt") as pfile:
    APP_PASSWORD = pfile.read().strip()
HEADERS = {
    "X-USER-TOKEN": APP_PASSWORD.strip()
}
pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"


def create_account():
    user_params = {
        "token": APP_PASSWORD,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }

    account_response = requests.post(url=pixela_endpoint,json=user_params)
    print(account_response.text)


#create_account()


def post_graph():
    graph_config = {
        "id": "graph1",
        "name": "Spanish Reading",
        "unit": "pages",
        "type": "int",
        "color": "sora",
    }
    response = requests.post(url=graph_endpoint, json=graph_config, headers=HEADERS)
    print(response.text)


def post_pixel():
    today_formated: str = today.date().strftime("%Y%m%d")
    pixel_config = {
       # "date": today_formated,
        "date": "20221219",
        "quantity": "0",
    }
    response = requests.post(url=pixel_endpoint, json=pixel_config, headers=HEADERS)
    print(response.text)

#create_account()
#post_graph()
post_pixel()