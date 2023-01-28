from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class IdLocatorTest:

    driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("http://practice.cybertekschool.com/multiple_buttons")

    dontClickButton=driver.find_element(By.ID, "disappearing_button")
    dontClickButton.click()

    time.sleep(3)
    driver.quit()