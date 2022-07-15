import os
import requests
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager

print("Welcome to M's Flight Club")
print("We find the best flight deals and email you")

if input("Do you have an account? yes / no ")=="no":
    first_name = input("What is your first name?\n")
    last_name = input("What is your last name?\n")
    email = input("What is your email?\n")
    email_check = input("Type your email again\n")
    while email_check != email:
        email_check = input("Emails don't match. Please type your email again\n")
    print("You're in the club!")
    
headers = {
    "Authorization": os.environ.get("authorization")
}

add = {
"user": {
    "firstName": first_name,
    "lastName": last_name,
    "email": email
}
} 

response = requests.post("https://api.sheety.co/13fe58756d09cfaa4bea89b12756f4f3/flightMinPrice/users", json=add, headers=headers) 
print("Your email has been added, check your inbox for good deals")

gsheet = DataManager()

for city in gsheet.data["prices"]:
    price = FlightData(city["iataCode"])
    if price.price<city["lowestPrice"]:
        NotificationManager(city["city"], price.price)
