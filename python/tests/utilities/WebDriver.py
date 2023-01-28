from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.ie.service import Service as IEService
from webdriver_manager.microsoft import IEDriverManager

class WebDriver:

    def getDriver(self,browserType):

        driver=None
        self.browserType=browserType

        if(self.browserType.lower()=="chrome"):
            driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager.install()))
        elif(self.browserType.lower()=="firefox"):
            driver=webdriver.Firefox(service=FirefoxService(GeckoDriverManager.install()))
        elif(self.browserType.lower()=="ie"):
            driver=webdriver.Ie(service=IEService(IEDriverManager.install()))

        return driver