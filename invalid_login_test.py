import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login_invalid_login():
    driver = webdriver.Edge()
    driver.get("https://www.saucedemo.com/")
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "input[placeholder='Username']").send_keys("invalid_user")
    driver.find_element(By.ID, "password").send_keys("invalid_password")
    time.sleep(10)
    driver.find_element(By.CSS_SELECTOR, "input[class='submit-button btn_action']").click()
    error_msg = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
    assert "login credential not matched" in error_msg
