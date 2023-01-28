from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

class NavigationDemo:

    driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.google.com")
    time.sleep(3)
    driver.get("https://www.facebook.com")
    time.sleep(3)
    driver.back()
    time.sleep(3)
    driver.forward()
    driver.quit()