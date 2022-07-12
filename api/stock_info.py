import requests
import datetime as dt
import smtplib
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_PRICE_API_KEY = os.environ.get("stock_price_api_key")
NEWS_API_KEY = os.environ.get("news_api_key")

EMAIL = os.environ.get("email")
PASSWORD = os.environ.get("password")

## STEP 1: Get stock price difference

today = dt.datetime.now()
day2 = (today - dt.timedelta(days=3)).strftime('%Y-%m-%d')
day1 = (today - dt.timedelta(days=4)).strftime('%Y-%m-%d')

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_PRICE_API_KEY
}

stock_response = requests.get("https://www.alphavantage.co/query", params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]
day2_price = float(stock_data[day2]["4. close"])
day1_price = float(stock_data[day1]["4. close"])

percentage = (day2_price-day1_price)*100/day2_price

updown = None

if percentage>5.0:
    updown = "up"
elif percentage<-5.0:
    updown = "down"

if updown:
    
## STEP 2: Get the first 3 news pieces for the COMPANY_NAME if difference in stock is huge

    news_parameters = {
        "q": "tesla",
        "from": day2,
        "sortBy": "publishedAt",
        "apiKey": NEWS_API_KEY
    }

    news_response = requests.get("https://newsapi.org/v2/everything", params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"]
    article1 = news_data[0]["title"].encode('ascii', 'ignore').decode('ascii')
    article2 = news_data[1]["title"].encode('ascii', 'ignore').decode('ascii')
    article3 = news_data[2]["title"].encode('ascii', 'ignore').decode('ascii')

    # STEP 3: Send email

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, to_addrs=os.environ.get("recipient_email"),
        msg=f"Subject:{STOCK} {int(percentage)}%\n\n{article1}\n\n{article2}\n\n{article3}")


