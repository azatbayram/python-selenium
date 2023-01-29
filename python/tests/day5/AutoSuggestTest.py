import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Keys, ActionChains

class AutoSuggestTest():

    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.yatra.com/")
    departFrom=driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
    departFrom.click()
    departFrom.send_keys("New Delhi")
    ActionChains(driver).key_down(Keys.ENTER).perform()
    #alert = driver.switch_to.alert
    #time.sleep(2)
    #alert.accept()


    time.sleep(5)
    driver.quit()
