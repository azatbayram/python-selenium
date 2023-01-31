import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class iFrameTest():

    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://practice.cybertekschool.com/iframe")

    #1. switch iframe by using is or name attribute
    driver.switch_to.frame("mce_0_ifr")
    time.sleep(2)
    textBox=driver.find_element(By.ID, "tinymce")
    textBox.clear()
    textBox.send_keys("Azat was here")
    driver.switch_to.default_content()
    time.sleep(3)

    #2. switch iframe by using index
    driver.switch_to.frame(0)
    time.sleep(2)
    textBox = driver.find_element(By.ID, "tinymce")
    textBox.clear()
    textBox.send_keys("Azat was here with index")
    driver.switch_to.parent_frame()
    time.sleep(3)

    # 3. switch iframe by using web element
    driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
    time.sleep(2)
    textBox = driver.find_element(By.ID, "tinymce")
    textBox.clear()
    textBox.send_keys("Azat was here with webelement")
    driver.switch_to.default_content()

    time.sleep(3)
    driver.quit()