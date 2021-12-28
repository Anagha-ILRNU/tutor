import time

from selenium.webdriver.common.by import By

from pageObjects.TutorLoginPage import LoginPage
from pageObjects.addeventPage import AddEventsPage
from utilities import XLUtils
from utilities.readproperties import ReadConfig
from selenium.webdriver.common.keys import Keys


#### Addevent,edit,delete,report,completed event)
class Test_AddEvent:
    loginURL = ReadConfig.getApplicationURL()
    email = ReadConfig.getemail()
    password = ReadConfig.getpassword()
    path = ".//testdata/Tutor addevent.xlsx"
    # logger = LogGen.loggen()
    XLUtils = "C:\\Users\\yoges\\PycharmProjects\\ilrnu\\utilities\\XLUtils.py"

    def test_addnewEvent(self, setup):
        # self.logger.info("******* Starting Test_001_DDT_Add event test **********")
        # self.logger.info("******* Starting Login DDT Test **********")
        self.driver = setup
        self.driver.get(self.loginURL)
        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickTutorLoginSubmit()
        self.ep = AddEventsPage(self.driver)
        self.ep.clickEventTab()
        self.ep.clickAddEventButton()

        self.rows = XLUtils.getRowCount(self.path, 'Addevent')
        print("Number of Rows in a Excel:", self.rows)
        lst_status = []

        for r in range(2, self.rows + 1):
            self.Eventmode = XLUtils.readData(self.path, 'Addevent', r, 1)
            self.Eventcategory = XLUtils.readData(self.path, 'Addevent', r, 2)
            self.Eventname = XLUtils.readData(self.path, 'Addevent', r, 3)
            self.Eventdescription = XLUtils.readData(self.path, 'Addevent', r, 4)
            self.Eventaddress = XLUtils.readData(self.path, 'Addevent', r, 5)
            self.Eventdate = XLUtils.readData(self.path, 'Addevent', r, 6)
            self.EStarttimehour = XLUtils.readData(self.path, 'Addevent', r, 7)
            self.EStarttimemin = XLUtils.readData(self.path, 'Addevent', r, 8)
            self.EEndtimehour = XLUtils.readData(self.path, 'Addevent', r, 9)
            self.EEndtimemin = XLUtils.readData(self.path, 'Addevent', r, 10)
            self.AMPM = XLUtils.readData(self.path, 'Addevent', r, 11)
            self.Picture = XLUtils.readData(self.path, 'Addevent', r, 12)
            self.Expected = XLUtils.readData(self.path, 'Addevent', r, 13)

            self.ep.enterEventName(self.Eventname)
            self.ep.getEventCategory()

            # self.ep.uploadPicture(self.Picture)
            self.ep.selectEventStartTime()
            self.ep.enterGetHourStartTime(self.EStarttimehour)
            self.ep.enterGetMinStartTime(self.EStarttimemin)
            self.ep.enterStartAMPM(self.AMPM)
            self.ep.selectEventEndTime()
            self.ep.enterGetHourEndTime(self.EEndtimehour)
            self.ep.enterGetMinEndTime(self.EEndtimemin)
            self.ep.enterEndAMPM(self.AMPM)
            self.ep.clickCheckBox()
            self.ep.selectFile()

            # self.ep.enterEventDate(self.Eventdate)
            self.ep.getTopFrame()
            # self.ep.switchTopFrame()
            self.ep.getMceEdit(self.Eventdescription)
            self.ep.switchToDefault()
            time.sleep(10)

            act_title = self.driver.title
            Expected_title = "Events page | @iLRNU"

            if act_title == Expected_title:
                if self.exp == "Pass":
                    self.lp.tutor_logout();

    # def test_editEvent(self, setup):
    # def test_deleteEvent(self,setup):
    # def test_reportEvent(self,setup):
    # def test_showMoreLess(self,setup):

# add events
# Edit events
# delete events
# report events
# publish events
# join event
