from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class CheckBoxTest:

    driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("http://practice.cybertekschool.com/dynamic_loading/1")

    username=driver.find_element(By.CSS_SELECTOR, "#username")
    print(username.is_displayed())

    driver.find_element(By.CSS_SELECTOR, "#start>button").click()
    time.sleep(5)
    print(username.is_displayed())

    time.sleep(3)
    driver.quit()