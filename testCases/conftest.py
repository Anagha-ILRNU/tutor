import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setup():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get = "https://uat.ilrnu.com/login/"
    driver.maximize_window()
    return driver


