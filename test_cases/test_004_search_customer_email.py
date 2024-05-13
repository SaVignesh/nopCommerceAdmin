import pytest

from page_objects.login_page import Login
from utilities.custom_logger import LogGen

class Test_004_SearchCustomerByEmail:
    logger = LogGen.loggen() #Creating logger object to store logs
    email = "victoria_victoria@nopCommerce.com"
    @pytest.mark.regression
    def test_search_customer_by_email(self, setup):
        self.logger.info("***Search Customers By Email***")
        self.driver = setup
        lp = Login(self.driver)
        dp = lp.login()  # Getting dashboard page object from login method
        cp = dp.go_to_customers_page()
        cp.enter_search_email(self.email)
        cp.click_search_customers()
        status = cp.search_customer_by_email(self.email)
        if status == True:
            assert True
            self.logger.info("***Search Customers By Email Test Passed***")
        elif status == False:
            self.logger.error("***Search Customers By Email Test Failed***")
            assert False


