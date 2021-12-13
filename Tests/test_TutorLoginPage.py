import pytest
from selenium import webdriver
from Pages.TutorLoginPage import LoginPage

class Test_001_Login():
    loginURL = "https://www.ilrnu.com/login"
    email = "yatutor200@gmail.com"
    password = "India@2020"

    def test_Login_title(self,setup):
        self.driver = setup
        self.driver.get(self.loginURL)
        act_title=self.driver.title
        self.driver.close()
        if act_title=="Login page | @iLRNU":
            assert True
        else:
            assert False

    def logintutor(self,setup):
        self.driver = setup
        self.driver.get(self.loginURL)
        self.lp=LoginPage(self.driver)
        self.lp.userProfile()
        self.lp.tutorLogin()
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        self.driver.close()
        if act_title=="My Dashboard | @iLRNU":
            assert True
        else:
            assert False

