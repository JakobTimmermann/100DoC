import requests
import pandas as pd
import os
SHEET_NAME = "users"
PROJECT_NAME = "flightDeals"
USER_NAME = os.environ["SHEETY_USERNAME"]
SHEETY_PASSWORD = os.environ["SHEETY_PASSWORD"]


print("Welcome to Daisys Flight Club.\nWe find the best flight deals and email you.")
first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
email = ""
verify_email = "."
while email != verify_email:
  email = input("What is your Email?\n")
  verify_email = input("Type your email again\n")
  if email != verify_email:
    print("Emails not matching. Try again")

sheety_endpoint= f"https://api.sheety.co/{USER_NAME}/{PROJECT_NAME}/{SHEET_NAME}"
sheety_header = {"Authorization": f"Bearer {SHEETY_PASSWORD}"}
sheet_response = requests.get(url=sheety_endpoint, headers=sheety_header)
sheet_data = pd.DataFrame(sheet_response.json()[SHEET_NAME])
idx = len(sheet_data) + 2
sheety_body = {"user": {"firstName": first_name, "lastName": last_name, "email": email}}
sheet_response = requests.put(
    url=sheety_endpoint + f"/{idx}",
    json=sheety_body,
    headers=sheety_header,
)

print(sheet_response.text)




