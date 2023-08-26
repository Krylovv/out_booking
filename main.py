from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

PATH = "/Users/kryloff/Documents/OutBooking/chromedriver-mac-arm64/chromedriver"
driver = webdriver.Chrome()

driver.get("http://94.188.35.81:8081")
driver.implicitly_wait(5)
search = driver.find_element(by=By.CLASS_NAME, value="input--DgMmg")
search.send_keys("Ale")
user = driver.find_element(by=By.CLASS_NAME, value="item--f7n44").click()
driver.implicitly_wait(5)
password = driver.find_element(by=By.CLASS_NAME, value="input--DgMmg")
password.send_keys("TEST")



time.sleep(5)
driver.quit()
