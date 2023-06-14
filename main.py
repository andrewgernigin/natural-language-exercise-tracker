# Sheety API Site
# https://sheety.co/
# Nutritionx natural language API
# https://www.nutritionix.com/business/api

import requests
from datetime import datetime
import os

APP_ID = os.environ["APP_ID"]
APP_KEY = os.environ["APP_KEY"]

endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

query = input("Tell me which exercise you did: ")

parameters = {
    "query": query,
    "gender": "male",
    "weight_kg": "77",
    "height_cm": "177",
}


response = requests.post(url=endpoint, json=parameters, headers=headers)
response.raise_for_status()
print(response)
result = response.json()
today = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")

sheety_endpoint = "https://api.sheety.co/94b23f7ecdea3c1c0065a3cb09286bc5/workoutTracking/workouts"
sheety_headers = {
    "Authorization": os.environ["SHEETY_TOKEN"]
}
for exercise in result["exercises"]:
    params = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": int(exercise["duration_min"]),
            "calories": int(exercise["nf_calories"])
        }
    }
    sheety_response = requests.post(url=sheety_endpoint, json=params, headers=sheety_headers)
    print(sheety_response)



