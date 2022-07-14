import requests
import datetime as dt
import os

class FlightData:

    def __init__(self, destination):

        headers = {
            "apikey": os.environ.get("apikey")
        }
        now = dt.datetime.now()
        today = now.strftime("%d/%m/%Y")

        parameters = {
            "fly_from": "LON",
            "fly_to": destination,
            "date_from": today,
            "date_to": today,
        }

        flights = requests.get("https://tequila-api.kiwi.com/v2/search?", params=parameters, headers=headers) 
        self.price = flights.json()["data"][0]["price"]


