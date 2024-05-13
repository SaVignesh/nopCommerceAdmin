import pytest
from page_objects.login_page import Login
from utilities.custom_logger import LogGen
import string
import random




class Test_003_AddCustomer:
    logger = LogGen.loggen() #Creating logger object to store logs

    def random__generator(self,size=8, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))

    @pytest.mark.smoke
    def test_customers_page(self, setup):
        self.logger.info("***Testing Customers Page Title***")
        self.driver = setup
        lp = Login(self.driver)
        dp = lp.login()  # Getting dashboard page object from login method
        dp.click_customers_sidemenu()
        dp.click_customers_sidemenu_option()  # Getting customers page object from dashboard method
        if self.driver.title == "Customers / nopCommerce administration":
            self.logger.info("***Opened Customers Page***")
            assert  True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_customersPageTitle.png")
            self.logger.error("***Customers Page was not opened***")
            assert False

    @pytest.mark.smoke
    def test_add_customers_page(self, setup):
        self.logger.info("***Testing Customers Page Title***")
        self.driver = setup
        lp = Login(self.driver)
        dp = lp.login()  # Getting dashboard page object from login method
        cp = dp.go_to_customers_page()  # Getting customers page object from dashboard method
        ac = cp.click_add_new()
        if self.driver.title == "Add a new customer / nopCommerce administration":
            self.logger.info("***Opened Add Customers Page***")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_customersPageTitle.png")
            self.logger.error("***Add Customers Page was not opened***")
            assert False


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_add_customer(self, setup):
        # Customer Details to be entered
        self.email = self.random__generator() + "@gmail.com"
        self.password = "test123"
        self.first_name = "Newman"
        self.last_name = "Human"
        self.gender = "Male"
        self.dob = "17/09/1990"
        self.company = "QA org"
        self.newsletter = "Your store name"
        self.role = "Guests"
        self.manager = "Vendor 2"
        self.comment = "Testing add customer"


        self.logger.info("***Testing Add Customer Functionality***")
        self.driver = setup
        lp = Login(self.driver)
        dp = lp.login()                 # Getting dashboard page object from login method
        cp = dp.go_to_customers_page()  # Getting customers page object from dashboard method
        ac = cp.click_add_new()
        ac.enter_email(self.email)
        ac.enter_password(self.password)
        ac.enter_first_name(self.first_name)
        ac.enter_last_name(self.last_name)
        ac.set_gender(self.gender)
        ac.enter_dob(self.dob)
        ac.enter_company_name(self.company)
        ac.select_newsletter(self.newsletter)
        ac.select_customer_roles(self.role)
        ac.select_manager_of_vendor(self.manager)
        ac.enter_admin_comment(self.comment)
        ac.click_save()
        d = ac.get_success_msg()
        print("Again")
        print(d)
        if "The new customer has been added successfully" in ac.get_success_msg():
            assert True
            self.logger.info("***Add Customer Test Passed***")
        else:
            self.logger.error("***Add Customer Test Failed")
            assert False




