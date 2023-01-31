import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Keys, ActionChains

class ScreenShotTest():

    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.yatra.com/")
    driver.find_element(By.CLASS_NAME, "dropdown-toggle").click()
    time.sleep(2)
    driver.find_element(By.ID, "signInBtn").click()
    time.sleep(2)
    driver.find_element(By.ID, "login-continue-btn").click()
    time.sleep(2)
    currentProjectPath=os.path.abspath("../")
    driver.get_screenshot_as_file(currentProjectPath+"/data/screenshot/test1.png")

    time.sleep(3)
    driver.quit()