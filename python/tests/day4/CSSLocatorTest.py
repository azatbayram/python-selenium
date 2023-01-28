from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class CSSLocatorTest:

    driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("http://practice.cybertekschool.com/multiple_buttons")

    button4=driver.find_element(By.CSS_SELECTOR, "button[onclick='button4()']")
    button4.click()


    time.sleep(3)
    driver.quit()