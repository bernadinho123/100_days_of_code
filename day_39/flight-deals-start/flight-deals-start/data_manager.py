import requests
from pprint import pprint

Sheety_prices_endpoint = 'https://api.sheety.co/b05326adb1293722ac3c6ccd0d1bbffb/flightDeals(day39)/prices'
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/b05326adb1293722ac3c6ccd0d1bbffb/flightDeals(day39)/users"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=Sheety_prices_endpoint)
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{Sheety_prices_endpoint}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_customer_emails(self):
        customers_endpoint = Sheety_prices_endpoint
        response = requests.get(url=customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
