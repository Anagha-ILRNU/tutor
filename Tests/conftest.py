import pytest
from selenium import webdriver
from Config.configuration import TestData


@pytest.fixture(params=["chrome"], scope='class')
def init__driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=TestData.FIREFOX_EXECUTABLE_PATH)
    if request.param == "edge":
        web_driver = webdriver.Edge(executable_path=TestData.EDGE_EXECUTABLE_PATH)
    request.cls.driver = web_driver
    yield
    web_driver.close()
