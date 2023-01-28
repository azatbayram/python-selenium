from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class Etsy:

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://www.etsy.com/?ref=lgo")
        searchBox = driver.find_element(By.ID, "global-enhancements-search-query")
        searchBox.send_keys("selenium")
        ActionChains(driver).key_down(Keys.ENTER).perform()
        time.sleep(3)
        driver.quit()




