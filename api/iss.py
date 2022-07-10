import requests
from datetime import datetime
import smtplib
import os

LAT = 51.509865
LNG = -0.118092

EMAIL = os.environ.get("your_email")
PASSWORD = os.environ.get("your_password")

#iss API
iss_info = requests.get("http://api.open-notify.org/iss-now.json")
iss_info.raise_for_status()
iss_longitude = float(iss_info.json()["iss_position"]["longitude"])
iss_latitude = float(iss_info.json()["iss_position"]["latitude"])

#check distance
def within_5(coor1, coor2):
    if coor1-coor2 <=5:
        return True
    elif coor2-coor1 <=5:
        return True
    else:
        return False

#sunrise+sunset API
parameters = {
    "lat": LAT,
    "lng": LNG,
    "formatted": 0
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

#time
time_now = datetime.now().hour

if within_5(LAT, iss_latitude) and within_5(LNG, iss_longitude):
    if time_now<=sunrise or time_now>=sunset:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=EMAIL,
            to_addrs=os.environ.get("recipient_email"),
            msg="Subject:Look Up\n\nYou can see the ISS")
            
            
