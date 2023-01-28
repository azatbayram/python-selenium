from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class PartialLinkTextLocatorTest:

    driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("http://practice.cybertekschool.com/dynamic_loading")

    example4Link=driver.find_element(By.PARTIAL_LINK_TEXT, "Example 4:")
    example4Link.click()


    time.sleep(3)
    driver.quit()