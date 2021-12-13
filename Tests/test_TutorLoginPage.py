import pytest
from selenium import webdriver
from Pages.TutorLoginPage import LoginPage


@pytest.mark.usefixtures("setup")
class Test_001_Login():
    email = "yatutor200@gmail.com"
    password = "India@2020"

    def test_Login_title(self,setup):
        self.driver = setup
        #self.driver.get(self.baseURL)
        act_title= self.driver.title
        self.driver.close()
        if act_title=="Login page | @iLRNU":
            assert True
        else:
            assert False

    def logintutor(self,setup):
        self.driver = setup
        #self.driver.get(self.baseURL)
        self.driver = setup
        self.lp=LoginPage(self.driver)
        self.lp.userProfile()
        self.lp.tutorLogin()
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        self.driver.close()
        if act_title=="My Dashboard | @iLRNU":
            assert True
        else:
            assert False






# class Test_Login(BaseTest):
#     def test_signup_link_visible(self):
#         self.loginpage = LoginPage(self.driver)
#         flag = self.loginpage.is_signup_link_exist()
#         assert flag
#
#     def test_login_page_title(self):
#         self.loginpage = LoginPage(self.driver)
#         title = self.loginpage.get_title(TestData.LOGIN_PAGE_TITLE)
#         assert title == TestData.LOGIN_PAGE_TITLE
#
#     def test_login(self, Email, Password):
#         self.loginPage = LoginPage(self.driver)
#         self.loginpage.do_login()

