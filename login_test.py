import time
from logging import exception

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_selection_state_to_be

from User_login import driver


def test_login():
    driver = webdriver.Edge()
    driver.get("https://www.saucedemo.com/")
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='Username']").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(10)
    driver.find_element(By.CSS_SELECTOR, "input[class='submit-button btn_action']").click()
    time.sleep(5)
    logo = driver.find_element(By.CLASS_NAME,"app_logo")
    if logo.text == "Swag Labs":
        print("we are logged in")
    current_url = driver.current_url
    print("Current url is:", current_url)










