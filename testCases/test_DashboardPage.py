from pageObjects.DashboardPage import DashboardPage
from pageObjects.TutorLoginPage import LoginPage


class Test_002_DashBoard:
    loginURL = "https://uat.ilrnu.com/login/"
    email = "yatutor200@gmail.com"
    password = "India@2020"

    def test_addSubject(self, setup):
        self.driver = setup
        self.driver.get(self.loginURL)
        self.lp = LoginPage(self.driver)
        self.lp.enterEmail(self.email)
        self.lp.enterPassword(self.password)
        self.lp.entertutorLoginSubmit()
        self.dp = DashboardPage(self.driver)
        self.dp.clickSubject()
        act_title = self.driver.title
        print(act_title)
        if act_title == "Tutors page | @iLRNU":
            assert True
        else:
            assert False
        self.driver.close()

    def test_createOpenSession(self, setup):
        self.driver = setup
        self.driver.get(self.loginURL)
        self.lp = LoginPage(self.driver)
        self.lp.enterEmail(self.email)
        self.lp.enterPassword(self.password)
        self.lp.entertutorLoginSubmit()
        self.dp = DashboardPage(self.driver)
        self.dp.clickCreateOpenSession()
        act_title = self.driver.title
        print(act_title)
        if act_title == "Session creation page | @iLRNU":
            assert True
        else:
            assert False
        self.driver.close()

    def test_startTutoring(self, setup):
        self.driver = setup
        self.driver.get(self.loginURL)
        self.lp = LoginPage(self.driver)
        self.lp.enterEmail(self.email)
        self.lp.enterPassword(self.password)
        self.lp.entertutorLoginSubmit()
        self.dp = DashboardPage(self.driver)
        self.dp.clickStartTutoring()
        act_title = self.driver.title
        print(act_title)
        if act_title == "Messages page | @iLRNU":
            assert True
        else:
            assert False
        self.driver.close()

    def test_addCourse(self, setup):
        self.driver = setup
        self.driver.get(self.loginURL)
        self.lp = LoginPage(self.driver)
        self.lp.enterEmail(self.email)
        self.lp.enterPassword(self.password)
        self.lp.entertutorLoginSubmit()
        self.dp = DashboardPage(self.driver)
        self.dp.clickCourse()
        act_title = self.driver.title
        print(act_title)
        if act_title == "Tutors page | @iLRNU":
            assert True
        else:
            assert False
        self.driver.close()

    def test_editProfile(self, setup):
        self.driver = setup
        self.driver.get(self.loginURL)
        self.lp = LoginPage(self.driver)
        self.lp.enterEmail(self.email)
        self.lp.enterPassword(self.password)
        self.lp.entertutorLoginSubmit()
        self.dp = DashboardPage(self.driver)
        self.dp.editProfile()
        act_title = self.driver.title
        print(act_title)
        if act_title == "My Dashboard | @iLRNU":
            assert True
        else:
            assert False
        self.driver.close()

    def test_viewProfile(self, setup):
        self.driver = setup
        self.driver.get(self.loginURL)
        self.lp = LoginPage(self.driver)
        self.lp.enterEmail(self.email)
        self.lp.enterPassword(self.password)
        self.lp.entertutorLoginSubmit()
        self.dp = DashboardPage(self.driver)
        self.dp.viewProfile()
        act_title = self.driver.title
        print(act_title)
        if act_title == "Alankar Yogeshwaran | Tutor @ iLRNU":
            assert True
        else:
            assert False
        self.driver.close()
