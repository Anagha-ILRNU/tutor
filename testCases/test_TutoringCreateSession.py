from pageObjects.DashboardPage import DashboardPage
from pageObjects.TutorLoginPage import LoginPage
from utilities.readproperties import ReadConfig

class Opensession:
    loginURL = ReadConfig.getApplicationURL()
    email = ReadConfig.getemail()
    password = ReadConfig.getpassword()
    path = "testdata/Tutor addsubject.xlsx"

    def __init__(self):
        self.driver = setup

    def test_createOpenSession(self, setup):
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
        else:
            assert False
        self.driver.close()

# Create session
# go to subjects
