from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class MultipleElements:

    driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("http://practice.cybertekschool.com/multiple_buttons")

    buttons=driver.find_elements(By.TAG_NAME, "button")
    print(len(buttons))

    for button in buttons:
        print(button.text)

    time.sleep(3)
    driver.quit()