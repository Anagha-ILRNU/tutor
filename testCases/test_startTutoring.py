from pageObjects.DashboardPage import DashboardPage
from pageObjects.TutorLoginPage import LoginPage


class Opensession:
    loginURL = "https://uat.ilrnu.com/login/"
    email = "yatutor200@gmail.com"
    password = "India@2020"


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
    else:
        assert False
    self.driver.close()
