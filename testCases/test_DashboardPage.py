import pytest
from pageObjects.DashboardPage import DashboardPage
from pageObjects.TutorLoginPage import LoginPage


class Test_DashBoardPage:
    loginURL = "https://uat.ilrnu.com/login/"
    email = "yatutor200@gmail.com"
    password = "India@2020"

    @pytest.mark.sanity
    def test_addSubject(self, setup):
        self.driver = setup
        self.driver.get(self.loginURL)
        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickTutorLoginSubmit()
        self.dp = DashboardPage(self.driver)
        self.dp.clickSubject()
        act_title = self.driver.title
        print(act_title)
        if act_title == "Tutors pag | @iLRNU":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshot\\" + "test_addSubject.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    def test_createOpenSession(self, setup):
        self.driver = setup
        self.driver.get(self.loginURL)
        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickTutorLoginSubmit()
        self.dp = DashboardPage(self.driver)
        self.dp.clickCreateOpenSession()
        act_title = self.driver.title
        print(act_title)
        if act_title == "Session creation page | @iLRNU":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshot\\" + "test_createOpenSession.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    def test_startTutoring(self, setup):
        self.driver = setup
        self.driver.get(self.loginURL)
        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickTutorLoginSubmit()
        self.dp = DashboardPage(self.driver)
        self.dp.clickStartTutoring()
        act_title = self.driver.title
        print(act_title)
        if act_title == "Messages page | @iLRNU":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshot\\" + "test_startTutoring.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    def test_addCourse(self, setup):
        self.driver = setup
        self.driver.get(self.loginURL)
        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickTutorLoginSubmit()
        self.dp = DashboardPage(self.driver)
        self.dp.clickCourse()
        act_title = self.driver.title
        print(act_title)
        if act_title == "Tutors page | @iLRNU":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshot\\" + "test_addCourse.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    def test_editProfile(self, setup):
        self.driver = setup
        self.driver.get(self.loginURL)
        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickTutorLoginSubmit()
        self.dp = DashboardPage(self.driver)
        self.dp.editProfile()
        act_title = self.driver.title
        print(act_title)
        if act_title == "My Dashboard | @iLRNU":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshot\\" + "test_editProfile.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    def test_viewProfile(self, setup):
        self.driver = setup
        self.driver.get(self.loginURL)
        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickTutorLoginSubmit()
        self.dp = DashboardPage(self.driver)
        self.dp.viewProfile()
        act_title = self.driver.title
        print(act_title)
        if act_title == "Alankar Yogeshwaran | Tutor @ iLRNU":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshot\\" + "test_editProfile.png")
            self.driver.close()
            assert False
