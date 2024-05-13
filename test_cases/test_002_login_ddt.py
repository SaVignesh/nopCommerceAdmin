import pytest
from page_objects.login_page import Login
from utilities import excel_utils
from utilities.custom_logger import LogGen
from utilities.read_config_properties import ReadConfig


class Test_002_Login_DDT:
    # Read URL from config.ini
    url = ReadConfig.get_base_url().strip('\"')
    logger = LogGen.loggen()
    path = ".//TestData/LoginData.xlsx"
    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("***Login test with different data from Excel file***")
        self.driver = setup
        lp = Login(self.driver)
        lp.open_login_page(self.url)
        self.rows = excel_utils.getRowCount(self.path, 'Sheet1')
        self.exp_title = "Dashboard / nopCommerce administration"
        self.lst_status = []
        for r in range(2, self.rows+1):
            self.username = excel_utils.readData(self.path, 'Sheet1', r, 1)
            self.password = excel_utils.readData(self.path, 'Sheet1', r, 2)
            self.exp_result = excel_utils.readData(self.path, 'Sheet1', r, 3)
            lp.enter_email(self.username)
            lp.enter_password(self.password)
            lp.click_login()
            if self.driver.title == self.exp_title:
                if self.exp_result == "Pass":
                    lp.click_logout()
                    self.logger.info("***Passed***")
                    self.lst_status.append("Pass")
                elif self.exp_result == "Fail":
                    self.logger.info("***Failed***")
                    self.lst_status.append("Fail")
            elif self.driver.title != self.exp_title:
                if self.exp_title == "Fail":
                    self.logger.info("***Passed***")
                    self.lst_status.append("Pass")
                elif self.exp_title == "Pass":
                    self.logger.info("***Failed***")
                    self.lst_status.append("Fail")

        if "Fail" not in self.lst_status:
            self.logger.info("***Login DDT Passed***")
            assert True
        else:
            self.logger.error("***Login DDT Failed***")
            assert False
