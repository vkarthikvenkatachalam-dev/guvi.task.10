import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login_and_extract_text():
    driver=webdriver.Edge()
    try:
        driver.get("https://www.saucedemo.com/")
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR,"input[placeholder='Username']").send_keys("standard_user")
        driver.find_element(By.ID,"password").send_keys("secret_sauce")
        time.sleep(7)
        driver.find_element(By.CSS_SELECTOR,"input[class='submit-button btn_action']").click()
        time.sleep(5)
        text=driver.find_element(By.TAG_NAME,"body").text
        with open("Web_page_task_11.txt","w",encoding="utf-8") as file:
            file.write(text)
            print("Successfully extracted text")
    finally:
        driver.quit()

if __name__ == "__main__":
   test_login_and_extract_text()











