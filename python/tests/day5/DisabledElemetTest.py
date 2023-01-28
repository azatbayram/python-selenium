from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class CheckBoxTest:

    driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("http://practice.cybertekschool.com/radio_buttons")

    greenButton=driver.find_element(By.CSS_SELECTOR, "#green")
    print(greenButton.is_enabled())

    time.sleep(3)
    driver.quit()