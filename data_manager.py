import requests

SHEET_ENDPOINT = "sheety endpoint"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):

        response = requests.get(url=SHEET_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_code(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            requests.put(
                url=f"{SHEET_ENDPOINT}/{city['id']}",
                json=new_data
            )
