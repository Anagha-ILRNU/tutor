import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setup():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver


# ############################### Pytest HTML report #################################
#
# # It is hook for Adding Environment info to HTML report
#
# def pytest_configure(config):
#     config.metadata['Project name'] = 'ilRNU application'
#     config.metadata['Modules Name'] = 'Add Subject'
#     config.metadata['Tester'] = 'Yogi'
#
# # Hook for delete/modify Environment info to HTML Report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)
