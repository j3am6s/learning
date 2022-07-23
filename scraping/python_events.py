from selenium import webdriver
from selenium.webdriver.common.by import By

PATH = "/usr/local/chromedriver/chromedriver"
driver = webdriver.Chrome(executable_path=PATH)

driver.get("https://python.org/")

dates = []
events = []

for i in range(5):
    dates.append((driver.find_element(By.XPATH, f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i+1}]/time')).text)
    events.append((driver.find_element(By.XPATH, f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i+1}]/a')).text)

dic = {j: {'time': dates[i], 'event': events[i]} for i in range(5) for j in range(5)}

print(dic)

driver.quit()
