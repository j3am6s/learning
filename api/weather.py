import requests
from twilio.rest import Client
import os


API_KEY = os.environ.get("api_key")
LAT = 35.6895
LONG = 139.6917
account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")

parameters = {
    "lat": LAT,
    "lon": LONG,
    "exclude": "current,minutely,daily",
    "appid": API_KEY
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()["hourly"]

def check_rain():
    for i in range(12):
        if data[i]["weather"][0]["id"]<700:
            return True
    return False

if check_rain():
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                        body="You should take an umbrella",
                        from_= os.environ.get("your_number"),
                        to=os.environ.get("recipient_number")
                    )

print(message.status)
