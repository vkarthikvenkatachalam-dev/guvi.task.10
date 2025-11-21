import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://www.saucedemo.com/")
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"input[placeholder='Username']").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
time.sleep(10)
driver.find_element(By.CSS_SELECTOR,"input[class='submit-button btn_action']").click()