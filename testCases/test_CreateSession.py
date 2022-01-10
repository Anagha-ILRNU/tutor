import time
import pytest
from selenium.webdriver.common.by import By
from pageObjects.TutorLoginPage import LoginPage
from pageObjects.addsubjectPage import AddSubjectPage
from pageObjects.createsessionPage import CreateSessionPage
from utilities import XLUtils
from utilities.readproperties import ReadConfig


class Test_Opensession:
    loginURL = ReadConfig.getApplicationURL()
    email = ReadConfig.getemail()
    password = ReadConfig.getpassword()
    path = "testdata/Create session.xlsx"

    # logger = LogGen.loggen()
    XLUtils = "C:\\Users\\yoges\\PycharmProjects\\ilrnu\\utilities\\XLUtils.py"

    # @pytest.mark.sanity
    # @pytest.mark.regression
    def test_createOpenSession_001(self, setup):
        # self.logger.info("******* Starting Test_001_DDT_Add event test **********")
        # self.logger.info("******* Starting Login DDT Test **********")
        # Validate the Title and Subject added - Tutor
        self.driver = setup
        self.driver.get(self.loginURL)
        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickTutorLoginSubmit()
        self.sessionpage = CreateSessionPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Createsession')
        print("Number of Rows in a Excel:", self.rows)
        lst_status = []

        for r in range(2, self.rows + 1):
            # Session Information
            self.Sessiontitle = XLUtils.readData(self.path, 'Createsession', r, 1)
            # Session Type
            self.liveTutoring = XLUtils.readData(self.path, 'Createsession', r, 2)
            self.inPersonTutoring = XLUtils.readData(self.path, 'Createsession', r, 3)
            # Address details for inPersonTutoring
            self.searchArea = XLUtils.readData(self.path, 'Createsession', r, 4)
            self.addressTitle = XLUtils.readData(self.path, 'Createsession', r, 5)
            self.houseFlat = XLUtils.readData(self.path, 'Createsession', r, 6)
            self.landmark = XLUtils.readData(self.path, 'Createsession', r, 7)
            self.houseFlat = XLUtils.readData(self.path, 'Createsession', r, 8)
            # Session Timezone
            self.sessiontimezone = XLUtils.readData(self.path, 'Createsession', r, 9)
            # Session date and time
            self.sessionMonth = XLUtils.readData(self.path, 'Createsession', r, 10)
            self.sessionYear = XLUtils.readData(self.path, 'Createsession', r, 11)
            self.sessionDay = XLUtils.readData(self.path, 'Createsession', r, 12)
            self.sessionHour = XLUtils.readData(self.path, 'Createsession', r, 13)
            self.sessionMin = XLUtils.readData(self.path, 'Createsession', r, 14)
            self.sessionAmPm = XLUtils.readData(self.path, 'Createsession', r, 15)
            self.sessionduration = XLUtils.readData(self.path, 'Createsession', r, 16)

            # Select Session Recurrence
            self.repeatEvery = XLUtils.readData(self.path, 'Createsession', r, 17)
            self.repeatEveryWeek = XLUtils.readData(self.path, 'Createsession', r, 18)
            self.repeatEveryday = XLUtils.readData(self.path, 'Createsession', r, 19)
            self.repeatonSunday = XLUtils.readData(self.path, 'Createsession', r, 20)
            self.repeatonMonday = XLUtils.readData(self.path, 'Createsession', r, 21)
            self.repeatonTuesday = XLUtils.readData(self.path, 'Createsession', r, 22)
            self.repeatonWednesday = XLUtils.readData(self.path, 'Createsession', r, 23)
            self.repeatonThursday = XLUtils.readData(self.path, 'Createsession', r, 24)
            self.repeatonFriday = XLUtils.readData(self.path, 'Createsession', r, 25)
            self.repeatonSaturaday = XLUtils.readData(self.path, 'Createsession', r, 26)
            self.repeatMonth = XLUtils.readData(self.path, 'Createsession', r, 27)
            self.repeatyear = XLUtils.readData(self.path, 'Createsession', r, 28)
            self.repeatEvery1 = XLUtils.readData(self.path, 'Createsession', r, 29)

            # Add a Student
            self.addStudent = XLUtils.readData(self.path, 'Createsession', r, 30)

            ##### Create session Information details
            self.sessionpage.clkcreateSessionHome()
            self.sessionpage.drpsubjectName()
            self.sessionpage.enterSessionTitle(self.Sessiontitle)
            self.sessionpage.selectSessiontype(self.liveTutoring)
            self.sessionpage.sessiontimeZone(self.sessiontimezone)
            self.sessionpage.sessionMonth(self.sessionMonth)
            self.sessionpage.sessionYear(self.sessionYear)
            self.sessionpage.sessionDay(self.sessionDay)
            self.sessionpage.sessionHour(self.sessionHour)
            self.sessionpage.sessionMin(self.sessionMin)
            self.sessionpage.sessionAmPm(self.sessionAmPm)
            self.sessionpage.addStudent(self.addStudent)
            # self.driver.close()
