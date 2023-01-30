import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class MutipleWindowsTest():

    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://practice.cybertekschool.com/windows")
    beforeTitle=driver.title
    print(beforeTitle)
    driver.find_element(By.LINK_TEXT, "Click Here").click()

    currentHandle=driver.current_window_handle
    allHandles=driver.window_handles

    for handle in allHandles:
        if(handle != currentHandle):
            driver.switch_to.window(handle)
            afterTitle=driver.title
            print(afterTitle)
            break

    driver.switch_to.window(currentHandle)
    print(driver.title)

    time.sleep(3)
    driver.quit()