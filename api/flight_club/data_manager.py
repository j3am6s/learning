import os
import requests

class DataManager:
    def __init__(self):
        headers = {
            "Authorization": os.environ.get("authorization")
        }
        iata = ["PAR", "BER", "TYO", "SYD", "IST", "KUL", "NYC", "SFO", "CPT"]
        for i in range(2, 11):
            change = {
                "price": {
                    'iataCode': iata[i-2],
                }
            }
            requests.put(f"https://api.sheety.co/13fe58756d09cfaa4bea89b12756f4f3/flightMinPrice/prices/{i}", json=change, headers=headers)
        response = requests.get("https://api.sheety.co/13fe58756d09cfaa4bea89b12756f4f3/flightMinPrice/prices", headers=headers) 
        self.data = response.json()
        
