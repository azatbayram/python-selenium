import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class ImplicitWaitTest():

    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://practice.cybertekschool.com/dynamic_loading/4")
    driver.implicitly_wait(10)
    text=driver.find_element(By.ID, "finish").text
    print(text)

    #time.sleep(3)
    driver.quit()