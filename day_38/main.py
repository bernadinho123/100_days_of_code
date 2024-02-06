import requests
from datetime import datetime
import os
nut_appId = "0b8e4c23"
nut_api_key = "fe4fe05a93b48ef3ff03f9bb82348bcb"
nut_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
weight = "74"
height = "178"
age = "18"
sheet_endpoint = "https://api.sheety.co/b05326adb1293722ac3c6ccd0d1bbffb/day38(myWorkouts)/workouts"
# gender = "masculine"
exercise_done = input("Tell me which exercises you did:\n")
headers = {
    "x-app-id": nut_appId,
    "x-app-key": nut_api_key,
}
params = {
    "query": exercise_done,
    # "gender": gender,
    "weight_kg": weight,
    "height_cm": height,
    "age": age,

}
response = requests.post(url=nut_endpoint, json=params, headers=headers)
print(response.json())
data_base = response.json()
today = datetime.now()
bearer_headers = {
    "Authorization": "Bearer 123456789be"
}
for exercise in data_base["exercises"]:
    sheet_params = {
        "workout": {
            "date": today.strftime("%Y/%m/%d"),
            "time": today.strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    ok = requests.post(url=sheet_endpoint, json=sheet_params,headers=bearer_headers)
    print(ok.text)