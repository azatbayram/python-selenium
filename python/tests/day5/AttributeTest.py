from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class AttributeTest:

    driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("http://practice.cybertekschool.com/radio_buttons")

    blueRadioButton=driver.find_element(By.CSS_SELECTOR, "#blue")

    print(blueRadioButton.get_attribute("id"))
    print(blueRadioButton.get_attribute("type"))
    print(blueRadioButton.get_attribute("color"))


    time.sleep(3)
    driver.quit()