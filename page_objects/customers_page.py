from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from page_objects.add_customer_page import AddCustomer


class Customers(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    lnk_addNewCustomer_xpath = "//a[@href='/Admin/Customer/Create']"
    txt_searchEmail_xpath = "//input[@id='SearchEmail']"
    txt_searchFirstName_xpath = "//input[@id='SearchFirstName']"
    txt_searchLastName_xpath = "//input[@id='SearchLastName']"
    btn_searchCustomers_xpath = "//button[@id='search-customers']"

    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"


    def click_add_new(self):
        self.driver.find_element(By.XPATH, self.lnk_addNewCustomer_xpath).click()
        ac = AddCustomer(self.driver)
        return ac
    def enter_search_email(self,email):
        self.driver.find_element(By.XPATH,self.txt_searchEmail_xpath).send_keys(email)

    def click_search_customers(self):
        self.driver.find_element(By.XPATH,self.btn_searchCustomers_xpath).click()

    def enter_search_first_name(self,first_name):
        self.driver.find_element(By.XPATH,self.txt_searchFirstName_xpath).send_keys(first_name)

    def enter_search_last_name(self,last_name):
        self.driver.find_element(By.XPATH,self.txt_searchLastName_xpath).send_keys(last_name)

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH,self.tableRows_xpath))

    def search_customer_by_email(self, email):
        flag = False
        for r in range(1,self.getNoOfRows()+1):
            self.email_id = self.driver.find_element(By.XPATH,"//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[2]").text
            if self.email_id == email:
                flag = True
                break
        return flag

    def search_customer_by_name(self, name):
        flag = False
        for r in range(1,self.getNoOfRows()+1):
            self.searched_name = self.driver.find_element(By.XPATH,"//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[3]").text
            print("Searched name:", self.searched_name)
            print("name:", name)
            if self.searched_name == name:
                print("Searched name:"+self.searched_name)
                print("name:" + name)
                flag = True
                break
        return flag

