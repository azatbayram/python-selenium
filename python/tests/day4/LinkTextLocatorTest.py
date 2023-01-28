from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class LinkTextLocatorTest:

    driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("http://practice.cybertekschool.com/dynamic_loading")

    example2Link=driver.find_element(By.LINK_TEXT, "Example 2: Element on the page that is rendered after the trigger")
    example2Link.click()


    time.sleep(3)
    driver.quit()