from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class NameLocatorTest:

    driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("http://practice.cybertekschool.com/sign_up")

    nameBox=driver.find_element(By.NAME, "full_name")
    emailBox=driver.find_element(By.NAME, "email")

    nameBox.send_keys("Azat Bayram")
    emailBox.send_keys("testemail@gmail.com")

    time.sleep(3)
    driver.quit()