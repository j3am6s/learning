import smtplib
import datetime as dt
from random import choice

today = dt.datetime.now()
EMAIL = ""
PASSWORD = ""

if today.weekday()==4:
    with open("smtp/quotes.txt","r") as file:
        quotes = file.readlines()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,
        to_addrs="",
        msg=f"Subject:Weekly Quote\n\n{choice(quotes)}")
