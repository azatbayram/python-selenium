from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class VerifyUrlChanged:

    driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()

    driver.get("http://practice.cybertekschool.com/forgot_password")

    emailBox=driver.find_element(By.NAME,"email")
    emailBox.send_keys("testemail@gmail.com")
    driver.find_element(By.ID,"form_submit").click()

    time.sleep(3)

    expectedURL = "http://practice.cybertekschool.com/email_sent"
    actualURL=driver.current_url

    if(actualURL==expectedURL):
        print("PASS")
    else:
        print("FAIL")

    driver.quit()