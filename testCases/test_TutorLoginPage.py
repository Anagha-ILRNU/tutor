import pytest
from selenium import webdriver
from pageObjects.TutorLoginPage import LoginPage


class Tutor_Login:
    loginURL = "https://uat.ilrnu.com/login/"
    email = "yatutor200@gmail.com"
    password = "India@2020"

    # Function for Login page Title
    def test_LoginPageTitle(self,setup):
        self.driver=setup
        self.driver.get(self.loginURL)
        act_title=self.driver.title
        print(act_title)
        self.driver.close()
        if act_title == "Login page | @iLRNU":
            assert True
        else:
            assert False
        return


    def test_tutorLogin(self,setup):
        self.driver = setup
        self.driver.get(self.loginURL)
        self.lp = LoginPage(self.driver)
        self.lp.enterEmail(self.email)
        self.lp.enterPassword(self.password)
        self.lp.entertutorLoginSubmit()
        act_title = self.driver.title
        print(act_title)
        if act_title == "My Dashboard | @iLRNU":
            assert True
        else:
            assert False
        self.driver.close()










