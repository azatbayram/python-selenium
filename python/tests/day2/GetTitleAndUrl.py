from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

class GetTitleAndUrl:
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("http://practice.cybertekschool.com")
    pageTitle = driver.title
    pageUrl = driver.current_url
    time.sleep(3)
    print(pageTitle)
    print(pageUrl)
    driver.quit()