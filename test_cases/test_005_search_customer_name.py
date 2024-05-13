import pytest
from page_objects.login_page import Login
from utilities.custom_logger import LogGen
from base.base_driver import BaseDriver

@pytest.mark.regression
class Test_005_SearchCustomerByName:
    logger = LogGen.loggen() #Creating logger object to store logs
    first_name = "Victoria"
    last_name = "Terces"
    @pytest.mark.regression
    def test_search_customer_by_name(self, setup):
        self.logger.info("***Search Customers By Name***")
        self.driver = setup
        lp = Login(self.driver)
        dp = lp.login()  # Getting dashboard page object from login method
        cp = dp.go_to_customers_page()
        cp.enter_search_first_name(self.first_name)
        cp.enter_search_last_name(self.last_name)
        cp.click_search_customers()
        full_name = self.first_name + ' ' +  self.last_name
        print("Full name = ", full_name)
        status = cp.search_customer_by_name(full_name)
        if status == True:
            assert True
            self.logger.info("***Search Customers By Email Test Passed***")
        elif status == False:
            self.logger.error("***Search Customers By Email Test Failed***")
            assert False


