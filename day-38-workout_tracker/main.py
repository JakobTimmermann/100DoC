import requests
import datetime as dt
import os

SHEET_NAME = "trackIt"
PROJECT_NAME = "myWorkoutTracker"
USER_NAME = os.environ["SHEETY_USERNAME"]
SHEETY_PASSWORD = os.environ["PASSWORD"]

nutritionix_api_id = "f68380b3"
nutritionix_api_key = "48271bcf2ec0666b34d534d614f7476d"
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = f"https://api.sheety.co/{USER_NAME}/{PROJECT_NAME}/{SHEET_NAME}"

nutritionix_headers = {
    "x-app-id": nutritionix_api_id,
    "x-app-key": nutritionix_api_key,
    "Content-Type": "application/json"
}


def process_exercise(body: dict, header: dict):
    response = requests.post(url=exercise_endpoint, json=body, headers=header)
    exercises = response.json()['exercises']
    erows = []
    for exercise in exercises:
        edict = {}
        edict["exercise"] = exercise["name"]
        edict["calories"] = exercise["nf_calories"]
        edict["duration"] = exercise["duration_min"]
        edict["date"] = dt.date.today().strftime("%d.%m.%Y")
        edict["time"] = dt.datetime.today().strftime("%H:%M")
        erows.append(edict)
    return erows


def post_exercise(exercise :dict):
    sheety_header = {"Authorization": f"Bearer {SHEETY_PASSWORD}"}
    sheety_body = {}
    sheety_body["trackit"] = exercise
    sheet_response = requests.post(url=sheety_endpoint, json=sheety_body, headers=sheety_header)


exercise_text = input("What did you do today? ")
nutritionix_body = {
    "query": exercise_text,
    "gender": "male",
    "weight_kg": 85.0,
    "height_cm": 185.00,
    "age": 33
}

exercises = process_exercise(body=nutritionix_body,header=nutritionix_headers)
for e in exercises:
    post_exercise(e)
