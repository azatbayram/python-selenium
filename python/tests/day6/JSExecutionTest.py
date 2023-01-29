import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains

class JSExecutionTest():

    driver=webdriver.Chrome()
    driver.maximize_window()
    #driver.get("http://practice.cybertekschool.com/")
    driver.execute_script("window.open('http://practice.cybertekschool.com/','_self');")
    time.sleep(2)
    """"
    for x in range(1,10):
        driver.execute_script("window.scrollBy(0,50)")
    """
    #dropdown=driver.execute_script("return document.getElementsByTagName('li')[12];")
    dropdown=driver.find_element(By.LINK_TEXT, "Dropdown")
    driver.execute_script("arguments[0].scrollIntoView(true);", dropdown)
    time.sleep(3)
    driver.execute_script("arguments[0].click();" , dropdown)

    time.sleep(3)
    driver.quit()