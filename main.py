from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

PATH = "/Users/kryloff/Documents/OutBooking/chromedriver-mac-arm64/chromedriver"
driver = webdriver.Chrome()

driver.get("http://94.188.35.81:8081")
driver.implicitly_wait(5)

# find user
search = driver.find_element(by=By.CLASS_NAME, value="input--DgMmg")
search.send_keys("Ale")
driver.find_element(by=By.CLASS_NAME, value="item--f7n44").click()

# type in password
with open('.env/secrets') as f:
    password_line = f.readlines()
password = driver.find_element(by=By.CLASS_NAME, value="input--DgMmg")
password.send_keys(password_line)
time.sleep(5)
driver.find_element(by=By.CLASS_NAME, value="keyboard-button.keyboard-submit-button").click()
time.sleep(5)

# logout section
driver.find_element(by=By.CLASS_NAME, value="ui-btn.ui-btn--secondary.ui-btn--small").click()
driver.find_element(by=By.CLASS_NAME, value="ui-btn.ui-btn--secondary.ui-btn--middle").click()


time.sleep(10)
driver.quit()
