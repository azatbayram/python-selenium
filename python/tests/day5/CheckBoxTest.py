from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class CheckBoxTest:

    driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("http://practice.cybertekschool.com/checkboxes")

    checkbox1=driver.find_element(By.ID, "box1")
    checkbox2=driver.find_element(By.ID, "box2")

    print(checkbox1.is_selected())
    print(checkbox2.is_selected())

    checkbox1.click()

    print(checkbox1.is_selected())
    print(checkbox2.is_selected())

    time.sleep(3)
    driver.quit()