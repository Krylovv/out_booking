import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("http://94.188.35.81:8081")
driver.implicitly_wait(5)


# login section
try:
    # find user
    search = driver.find_element(by=By.CLASS_NAME, value="input--DgMmg")
    search.send_keys("Ale")
    time.sleep(1)
    driver.find_element(by=By.CLASS_NAME, value="item--f7n44").click()
    time.sleep(1)

    # type in password
    with open('.env/secrets') as f:
        password_line = f.readlines()
    password = driver.find_element(by=By.CLASS_NAME, value="input--DgMmg")
    password.send_keys(password_line)
    time.sleep(1)
    driver.find_element(by=By.CLASS_NAME, value="keyboard-button.keyboard-submit-button").click()
    time.sleep(1)
except:
    print("!!!!!!!!!!!!!!!!!!!!!!!!!")
    pass

# counter of layers for exit clicks
steps_counter = 1

# date chooser section
try:
    driver.find_element(by=By.XPATH, value="//span[text()='Дата']").click()
    time.sleep(1)
    date = '31'
    driver.find_element(by=By.XPATH, value="//div[text()={}]".format(date)).click()
    time.sleep(1)
    steps_counter += 1
except:
    print("Troubles with DATE  !!!!!!!!!!!!")
    pass

# movie selection
try:
    movie = '\"Рай и ад\"'
    driver.find_element(by=By.XPATH, value="//div[text()={}]".format(movie)).click()
    time.sleep(3)
except:
    print("Troubles with MOVIE  !!!!!!!!!!!!")
    pass



# logout section
try:
    for i in range(steps_counter):
        driver.find_element(by=By.TAG_NAME, value="path").click()
        time.sleep(1)
except:
    print("Troubles with svg click!!!!!!!!!!!!")
    pass

try:
    driver.find_element(by=By.CLASS_NAME, value="ui-btn.ui-btn--secondary.ui-btn--small").click()
    time.sleep(3)
    driver.find_element(by=By.XPATH, value="//span[text()='Закрыть смену']").click()
    # driver.find_element(by=By.CLASS_NAME, value="ui-btn.ui-btn--secondary.ui-btn--middle").click()
    time.sleep(3)
except:
    print("Troubles with logout!!!!!!!!!!!!")
    pass


time.sleep(40)
driver.quit()
