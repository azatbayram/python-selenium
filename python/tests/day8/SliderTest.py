import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class SliderTest():

    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.snapdeal.com/search?keyword=phone&santizedKeyword=&catId=&categoryId=0&suggested=true&vertical=&noOfResults=20&searchState=&clickSrc=suggested&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy")

    sliderLeft=driver.find_element(By.XPATH, "//a[contains(@class, 'left-handle')]")
    sliderRigt=driver.find_element(By.XPATH, "//a[contains(@class, 'right-handle')]")

    action=ActionChains(driver)
    #action.drag_and_drop_by_offset(sliderLeft, 60, 0).perform()
    #action.click_and_hold(sliderLeft).pause(1).move_by_offset(20, 0).release().perform()
    #action.drag_and_drop_by_offset(sliderRigt, -60, 0).perform()
    action.click_and_hold(sliderRigt).pause(1).move_by_offset(-80, 0).release().perform()

    time.sleep(5)
    driver.quit()