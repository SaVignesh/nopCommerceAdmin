from selenium import webdriver
import pytest
from page_objects.login_page import Login
from utilities.custom_logger import LogGen
from utilities.read_config_properties import ReadConfig


class Test_001_Login:


    #Read URL, email and password from config.ini
    url = ReadConfig.get_base_url().strip('\"')
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()

    logger = LogGen.loggen() #Creating logger object to store logs
    @pytest.mark.smoke
    def test_login_page_title(self, setup):

        self.logger.info("***Verifying home page title***")
        self.driver = setup
        lp = Login(self.driver)
        lp.open_login_page(self.url)
        if self.driver.title == "Your store. Login":
            assert True
            self.logger.info("*** Home page title test  passed***")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.logger.info("*** Home page title test  failed***")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.driver = setup
        self.logger.info("***Testing Login functionality***")
        lp = Login(self.driver)
        lp.open_login_page(self.url)
        lp.enter_email(self.email)
        lp.enter_password(self.password)
        lp.click_login()
        if self.driver.title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("***Login functionality Test Passed***")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_dashboardPageTitle.png")
            self.logger.info("***Login functionality Test Failed***")
            assert False
