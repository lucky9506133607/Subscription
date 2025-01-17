import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service




@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
        print("Launching chrome browser.........")
    elif browser=='firefox':
        driver = webdriver.Firefox()
        print("Launching firefox browser.........")
    else:
        driver = webdriver.Ie()
    return driver

def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

#######################pytest html report ###########################
# it hooks for adding environment info to html report
"""def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'customer'
    config._metadata['Tester'] = 'Lucky'"""

def pytest_configure(config):
    config.addinivalue_line("markers", "browser: mark test to run only on specific browser")

"""@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)"""

def pytest_metadata(metadata):
    metadata['Project Name'] = 'nop Commerce'
    metadata['Module Name'] = 'customer'
    metadata['Tester'] = 'Lucky'