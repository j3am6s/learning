import smtplib
import datetime as dt
from random import choice
import os

today = dt.datetime.now()
EMAIL = os.environ.get("your_email")
PASSWORD = os.environ.get("your_password")

if today.weekday()==4:
    with open("smtp/quotes.txt","r") as file:
        quotes = file.readlines()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,
        to_addrs=os.environ.get("recipient_email"),
        msg=f"Subject:Weekly Quote\n\n{choice(quotes)}")
