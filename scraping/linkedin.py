PASSWORD = ""
EMAIL = ""
FIRST_NAME = ""
LAST_NAME = ""

URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PATH = "/usr/local/chromedriver/chromedriver"
driver = webdriver.Chrome(executable_path=PATH)

driver.get(URL)

driver.find_element(By.LINK_TEXT, "Sign in").click()

username = driver.find_element(By.ID, "username")
username.send_keys(EMAIL)
password = driver.find_element(By.ID, "password")
password.send_keys(PASSWORD)
button = driver.find_element(By.CSS_SELECTOR, ".login__form_action_container  button")
button.click()

save = driver.find_element(By.CSS_SELECTOR, ".mt5 .display-flex button .jobs-save-button artdeco-button artdeco-button--3 artdeco-button--secondary")
save.click()
