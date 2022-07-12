import requests
import os

APP_ID = os.environ.get("app_id")
API_KEY = os.environ.get("api_key")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": input("What did you do? "),
    "gender": "male",
    "weight_kg": 82.8,
    "height_cm": 184.1,
    "age": 24
}

response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", json=parameters, headers=headers)
data = response.json()
needed = data["exercises"][0]

import datetime as dt

now = dt.datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%X")

headers_sheet = {
    "Authorization": os.environ.get("authorization")
}

add = {
    'workout':{
        "date": date,
        "time": time,
        "exercise": needed["name"].title(),
        "duration": needed["duration_min"],
        "calories": needed["nf_calories"],
    }
}

add = requests.post("https://api.sheety.co/13fe58756d09cfaa4bea89b12756f4f3/workoutSheet/workouts", json=add, headers=headers_sheet) 
