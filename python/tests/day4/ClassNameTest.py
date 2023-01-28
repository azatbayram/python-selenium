from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class ClassNameTest:

    driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("http://practice.cybertekschool.com/sign_up")

    time.sleep(2)

    homeLink=driver.find_element(By.CLASS_NAME, "nav-link")
    homeLink.click()

    time.sleep(3)
    driver.quit()