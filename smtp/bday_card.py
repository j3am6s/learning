import os
import smtplib
import datetime as dt
import pandas as pd
import random

EMAIL = os.environ.get("your_email")
PASSWORD = os.environ.get("your_password")

now = dt.datetime.now()
month = now.month
day = now.day

people = pd.read_csv("birthdays.csv")
people = people.to_dict(orient="records")

for person in people:
    if person["month"]==month and person["day"]==day:
        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt", "r") as file:
            card = file.read()
        card = card.replace("[NAME]", person["name"])
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=EMAIL, to_addrs=os.environ.get("person_who_s_birthday_it_is"),
            msg=f"Subject:Happy Birthday\n\n{card}")


