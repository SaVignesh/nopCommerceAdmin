
from selenium import webdriver
import pytest
from pytest_metadata.plugin import metadata_key
@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option("detach", True)
        opt.add_argument("--disable-notifications")
        driver = webdriver.Chrome(options=opt)
        driver.maximize_window()
    elif browser == "firefox":
        driver = webdriver.Firefox()
        driver.maximize_window()
    elif browser == "edge":
        driver = webdriver.Edge()
        driver.maximize_window()
    else:
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=opt)
        driver.maximize_window()
    yield driver
    driver.close()

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

def pytest_html_report_title(report):
    report.title = "nop Commerce Admin Website Report"



def pytest_configure(config):

    config.stash[metadata_key]["Project Name"] = "nop Commerce"
    config.stash[metadata_key]["Module Name"] = "Customers"
    config.stash[metadata_key]["Tester"] = "Vigneshwar"


