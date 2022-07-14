import smtplib
import requests
import os 

class NotificationManager:
    
    def __init__(self, city, price):

        EMAIL = os.environ.get("email")
        PASSWORD = os.environ.get("password")

        headers = {
            "Authorization": os.environ.get("authorization")
        }

        response = requests.get("https://api.sheety.co/13fe58756d09cfaa4bea89b12756f4f3/flightMinPrice/users", headers=headers) 
        response.raise_for_status()
        data = response.json()["users"]

        for email in data : 
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
                connection.login(user=EMAIL, password=PASSWORD)
                connection.sendmail(from_addr=EMAIL, to_addrs=email["email"],
                msg=f"Subject:Cheap flight!!\n\nGo to {city} for {price}$ only!!!")
