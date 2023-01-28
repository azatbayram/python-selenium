from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class DropDownTest:

    driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("http://practice.cybertekschool.com/dropdown")

    driver.find_element(By.ID, "dropdownMenuLink").click()
    time.sleep(2)
    dropdownOptions=driver.find_elements(By.CLASS_NAME, "dropdown-item")

    for options in dropdownOptions:
        print(options.text)

    dropdownOptions[2].click()

    time.sleep(3)
    driver.quit()