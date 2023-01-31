import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import ElementNotVisibleException


class ExplicitWaitTest():

    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://practice.cybertekschool.com/dynamic_loading/1")
    driver.implicitly_wait(10)

    driver.find_element(By.TAG_NAME, "button").click()
    userinput = driver.find_element(By.ID, "username")

    wait=WebDriverWait(driver, 10, 2, ignored_exceptions=[ElementNotVisibleException])
    wait.until(ec.visibility_of(userinput))

    userinput.send_keys("Azat Bayram")

    time.sleep(3)
    driver.quit()