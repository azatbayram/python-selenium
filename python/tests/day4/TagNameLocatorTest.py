from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class TagNameLocatorTest:

    driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("http://practice.cybertekschool.com/sign_up")

    nameBox=driver.find_element(By.TAG_NAME, "input")

    nameBox.send_keys("Azat Bayram with tag name locator")

    time.sleep(3)
    driver.quit()