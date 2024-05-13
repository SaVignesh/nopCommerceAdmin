from selenium.webdriver.common.by import By

from page_objects.dashboard_page import Dashboard
from base.base_driver import BaseDriver
from utilities.read_config_properties import ReadConfig


class Login(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    txt_username_xpath = "//input[@id= 'Email']"
    txt_password_xpath = "//input[@id = 'Password']"
    btn_signin_xpath = "//button[@type= 'submit']"
    lnk_logout_xpath = "//a[text()='Logout']"



    def open_login_page(self, url):
        self.driver.get(url)


    def enter_email(self, email):
        self.driver.find_element(By.XPATH, self.txt_username_xpath).clear()   # Clear Text Box
        self.driver.find_element(By.XPATH, self.txt_username_xpath).send_keys(email)  # Enter Email Address

    def enter_password(self, password):
        self.driver.find_element(By.XPATH,self.txt_password_xpath).clear()  # Clear Text Box
        self.driver.find_element(By.XPATH, self.txt_password_xpath).send_keys(password)  # Enter Password

    def click_login(self):
        self.driver.find_element(By.XPATH, self.btn_signin_xpath).click()

    def click_logout(self):

        if self.driver.capabilities['browserName'].lower() == "firefox" :
                self.blocking_element = self.driver.find_element(By.XPATH, "//div[@ id='ajaxBusy']")
                self.wait_for_element_invisible(self.blocking_element)
                self.driver.find_element(By.XPATH, self.lnk_logout_xpath).click()

        else:
            self.driver.find_element(By.XPATH, self.lnk_logout_xpath).click()
                #assert False



    # login action in single function
    # to be used when testing functionality of other pages and need to login first
    def login(self):
        # Read URL, email and password from config.ini
        url = ReadConfig.get_base_url().strip('\"')
        email = ReadConfig.get_email()
        password = ReadConfig.get_password()
        self.open_login_page(url)
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()
        # Creating a dashboard page object and return it
        # This is so we do not need to create separate Login page object for testing other pages
        dp = Dashboard(self.driver)
        return dp





