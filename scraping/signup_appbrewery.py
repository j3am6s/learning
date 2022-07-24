from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PATH = "/usr/local/chromedriver/chromedriver"
driver = webdriver.Chrome(executable_path=PATH)

driver.get("http://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element(By.NAME, "fName")
fname.send_keys("Robert")
lname = driver.find_element(By.NAME, "lName")
lname.send_keys("Miller")
email = driver.find_element(By.NAME, "email")
email.send_keys("robert.miller@fakegmail.com")

button = driver.find_element(By.CSS_SELECTOR, "form button")
button.click()

driver.quit()

