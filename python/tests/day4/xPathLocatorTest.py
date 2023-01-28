from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class xPathLocatorTest:

    driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("http://practice.cybertekschool.com/multiple_buttons")

    button2=driver.find_element(By.XPATH, "//button[@onclick='button2()']")
    button2.click()


    time.sleep(3)
    driver.quit()
