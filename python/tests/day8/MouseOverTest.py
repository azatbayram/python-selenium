import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class MouseOverTest():

    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://practice.cybertekschool.com/hovers")

    imgs=driver.find_elements(By.XPATH, "//div[@class='figure']")
    action=ActionChains(driver)

    for img in imgs:
        action.move_to_element(img).perform()
        time.sleep(2)


    time.sleep(3)
    driver.quit()