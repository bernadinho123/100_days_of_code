import requests

Sheety_prices_endpoint = 'https://api.sheety.co/b05326adb1293722ac3c6ccd0d1bbffb/flightDeals(day39)/prices'


class DataManager:
    def __init__(self):
        self.destination_data = {}

    # This class is responsible for talking to the Google Sheet.

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
