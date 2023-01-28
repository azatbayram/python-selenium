from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class VerifyConfirmatonMessage:
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    expectedEmail="testemail@gmail.com"

    driver.get("http://practice.cybertekschool.com/forgot_password")

    emailBox = driver.find_element(By.NAME, "email")
    emailBox.send_keys(expectedEmail)

    time.sleep(3)

    actualEmail=emailBox.get_attribute("value")

    if (actualEmail==expectedEmail):
        print("PASS")
    else:
        print("FAIL")

    driver.quit()



