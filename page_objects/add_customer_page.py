from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from base.base_driver import BaseDriver


class AddCustomer(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    txt_email_xpath = "//input[@id='Email']"
    txt_password_xpath = "//input[@id='Password']"
    txt_firstName_xpath = "//input[@id='FirstName']"
    txt_lastName_xpath = "//input[@id='LastName']"
    rd_genderMale_xpath = "//input[@id='Gender_Male']"
    rd_genderFemale_xpath = "//input[@id='Gender_Female']"
    txt_dob_xpath = "//input[@id='DateOfBirth']"
    txt_company_xpath = "//input[@id='Company']"
    txt_newsletter_xpath = "//div[@class='input-group-append']//div[@class='input-group']"
    lst_testStore2_xpath = "//li[text()='Test store 2']"
    lst_yourStoreName_xpath = "//li[text()='Your store name']"
    txt_customerRoles_xpath = "//div[@class='input-group-append input-group-required']//div[@class='input-group']"
    lst_administratorRole_xpath = "//li[text()='Administrators']"
    lst_forumModeratorRole_xpath = "//li[text()='Forum Moderators']"
    lst_alreadySelectedRegisteredRole = "//li[@role='option' and text()='Registered']"
    lst_registeredRole_xpath ="//li[text()='Registered']"
    lst_guestsRole_xpath = "//li[text()='Guests']"
    lst_vendorsRole_xpath = "//li[text()='Vendors']"

    drp_managerOrVendor_xpath = "//select[@id='VendorId']"
    txt_adminComment_xpath = "//textarea[@id='AdminComment']"
    btn_save_xpath = "//div[@class='float-right']//button[@name='save']"

    txt_search_email = "//input[@id='SearchEmail']"
    txt_search_first_name = "//input[@id='SearchFirstName']"
    txt_search_last_name = "//input[@id='SearchLastName']"
    btn_search_customers = "//button[@id='search-customers']"





    def enter_email(self, email):
        #self.wait_for_element(self.txt_email_xpath).send_keys(email)
        self.driver.find_element(By.XPATH, self.txt_email_xpath).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.txt_password_xpath).send_keys(password)

    def enter_first_name(self, first_name):
        self.driver.find_element(By.XPATH, self.txt_firstName_xpath).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(By.XPATH, self.txt_lastName_xpath).send_keys(last_name)

    def set_gender(self, gender):
        if gender.lower() == "male":
            self.driver.find_element(By.XPATH, self.rd_genderMale_xpath)
        if gender.lower() == "female":
            self.driver.find_element(By.XPATH, self.rd_genderFemale_xpath)
        else:
            self.driver.find_element(By.XPATH, self.rd_genderMale_xpath)

    def enter_dob(self,dob):
        self.driver.find_element(By.XPATH, self.txt_lastName_xpath).send_keys(dob)

    def enter_company_name(self,company):
        self.driver.find_element(By.XPATH, self.txt_company_xpath).send_keys(company)

    def select_newsletter(self,newsletter):
        self.driver.find_element(By.XPATH, self.txt_newsletter_xpath).click()
        if newsletter.lower() == "test store 2":

            self.driver.find_element(By.XPATH,self.lst_testStore2_xpath).click()
        elif newsletter.lower() == "your store name":

            self.driver.find_element(By.XPATH,self.lst_yourStoreName_xpath).click()


    def select_customer_roles(self,role):
        self.driver.find_element(By.XPATH, self.txt_customerRoles_xpath).click()
        self.driver.find_element(By.XPATH, self.lst_alreadySelectedRegisteredRole).click()
        if role.lower() == "administrators":
            self.driver.find_element(By.XPATH,self.lst_administratorRole_xpath).click()
        elif role.lower() == "forum moderators":
            self.driver.find_element(By.XPATH,self.lst_forumModeratorRole_xpath).click()
        elif role.lower() == "registered":
            self.driver.find_element(By.XPATH,self.lst_registeredRole_xpath).click()
        elif role.lower() == "guests":
            self.driver.find_element(By.XPATH,self.lst_guestsRole_xpath).click()
        elif role.lower() == "vendors":
            self.driver.find_element(By.XPATH,self.lst_vendorsRole_xpath).click()
        else:
            self.driver.find_element(By.XPATH,self.lst_guestsRole_xpath).click()

    def select_manager_of_vendor(self,manager):
        drp = Select(self.driver.find_element(By.XPATH,self.drp_managerOrVendor_xpath))
        drp.select_by_visible_text(manager)

    def enter_admin_comment(self,comment):
        self.driver.find_element(By.XPATH, self.txt_adminComment_xpath).send_keys(comment)

    def click_save(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()

    def get_success_msg(self):
        return (self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissable']").text)













