from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
import time

class SelectDropdownTest:

    driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("http://practice.cybertekschool.com/dropdown")

    states=driver.find_element(By.ID, "state")
    select=Select(states)

    select.select_by_visible_text("Alaska")

    time.sleep(3)
    driver.quit()