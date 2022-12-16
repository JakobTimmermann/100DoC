import requests

parameters = {
    "amount": 10,
    "type": "boolean",
    }
response = requests.get("https://opentdb.com/api.php",params=parameters)
questions_data = response.json()["results"]
