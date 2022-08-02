from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import schedule

PATH = "/usr/local/chromedriver/chromedriver"
driver = webdriver.Chrome(executable_path=PATH)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")
start_time = time.time()


def expensive(money, prices):
    for i in range(8):
        if prices[i]>money:
            return prices[i-1]

def upgrades():
    price = driver.find_elements(By.CSS_SELECTOR, "#store div b")
    prices = []
    for i in range(8):
        p = price[i].text.split(" - ")[1].replace(",", "")
        prices.append(int(p))
    money = int(driver.find_element(By.ID, "money").text.replace(",",""))
    price[prices.index(expensive(money, prices))].click()

schedule.every(5).seconds.do(upgrades)

while time.time() - start_time < 300:
    schedule.run_pending()
    cookie.click()

print(driver.find_element(By.ID, "cps").text)

driver.quit()
