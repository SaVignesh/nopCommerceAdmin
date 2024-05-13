from selenium.webdriver.common.by import By
from page_objects.customers_page import Customers
from base.base_driver import BaseDriver



class Dashboard(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    lnk_customerssidemenu_xpath = "//a[contains(@href,'#')]//p[contains(text(),'Customers')]"
    lnk_customersoption_xpath = "//a[@href = '/Admin/Customer/List']"

    # Page Titles
    dashboard_page_title = "Dashboard / nopCommerce administration"
    customers_page_title = "Customers / nopCommerce administration"

    def click_customers_sidemenu(self):
        self.driver.find_element(By.XPATH, self.lnk_customerssidemenu_xpath).click()  # Click Customers Sidebar

    def click_customers_sidemenu_option(self):
        self.driver.find_element(By.XPATH, self.lnk_customersoption_xpath).click()  # Click Customers Option

    def go_to_customers_page(self):
        self.click_customers_sidemenu()
        self.click_customers_sidemenu_option()
        cp = Customers(self.driver)
        return cp





