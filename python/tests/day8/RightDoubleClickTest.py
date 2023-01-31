import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class RightDoubleClickTest():

    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demo.guru99.com/test/simple_context_menu.html")

    action=ActionChains(driver)
    rightClick=driver.find_element(By.CSS_SELECTOR, ".context-menu-one.btn.btn-neutral")
    doubleClick=driver.find_element(By.XPATH, "(//button)[1]")

    #Right Click
    action.context_click(rightClick).perform()
    time.sleep(2)

    #Double Click
    #action.double_click(doubleClick).perform()


    time.sleep(3)
    driver.quit()