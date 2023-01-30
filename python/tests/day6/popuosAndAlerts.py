import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class popupsAndAlerts():

    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://practice.cybertekschool.com/javascript_alerts")

    JSAlert=driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
    JSConfirm=driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")
    JSPrompt=driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")

    JSAlert.click()
    alert=driver.switch_to.alert
    time.sleep(2)
    alert.accept()
    JSConfirm.click()
    time.sleep(2)
    alert.dismiss()
    JSPrompt.click()
    time.sleep(2)
    alert.send_keys("azat")
    alert.accept()

    time.sleep(3)
    driver.quit()