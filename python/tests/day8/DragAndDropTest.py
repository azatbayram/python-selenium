import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class DragAndDropTest():

    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demos.telerik.com/kendo-ui/dragdrop/index")

    drag=driver.find_element(By.ID, "draggable")
    drop=driver.find_element(By.ID, "droptarget")

    action=ActionChains(driver)
    drop.find_element(By.XPATH, "//*[.='Accept Cookies']").click()
    time.sleep(2)
    action.drag_and_drop(drag,drop).perform()

    time.sleep(5)
    driver.quit()