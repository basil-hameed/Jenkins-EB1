"""
LoginPage.py contains all the methods related to the login page

PageObjects File
"""
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# import the data and locator
from TestData.data import OrangeHRMData
from TestLocators.locators import OrangeHRMLocator

class HRMLoginPage:
    # create the chrome driver object
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # start() method to launch the url
    def start(self):
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(OrangeHRMData.url)
        return True
    
    # login() method to perform orangehrm login
    def login(self):
        self.driver.find_element(by=By.NAME, value=OrangeHRMLocator.username_locator).send_keys(OrangeHRMData.username)
        self.driver.find_element(by=By.NAME, value=OrangeHRMLocator.password_locator).send_keys(OrangeHRMData.password)
        self.driver.find_element(by=By.XPATH, value=OrangeHRMLocator.login_button_locator).click()
        return True
    
    # shutdown() method to quit the driver
    def shutdown(self):
        self.driver.quit()
        return None