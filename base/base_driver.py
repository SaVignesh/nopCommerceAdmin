from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Class for storing general driver functionality like explicit waits
class BaseDriver:
    def __init__(self, driver):
        self.driver = driver

    # wait for element to be loaded in webpage
    # to be used when a page is very slow to load
    def wait_for_element(self, element):
        mywait = WebDriverWait(self.driver,10)
        element = mywait.until(EC.presence_of_element_located((By.XPATH,element)))
        return element

    def wait_for_element_click(self, element):
        mywait = WebDriverWait(self.driver,10)
        element = mywait.until(EC.element_to_be_clickable((By.XPATH,element)))
        return element

    def wait_for_element_invisible(self,element):
        mywait = WebDriverWait(self.driver, 10)
        element = mywait.until(EC.invisibility_of_element_located(element))
        return