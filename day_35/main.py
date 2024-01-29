import requests

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "cab9ee8e5fcda68746ce3b191aecce39"

weather_param = {
    "lat": -22.906847,
    "lon": -43.172897,
    "appid": api_key,
    "cnt": 4,
}
response = requests.get(OWN_Endpoint, params=weather_param)
response.raise_for_status()
weather_data = response.json()
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella.")
