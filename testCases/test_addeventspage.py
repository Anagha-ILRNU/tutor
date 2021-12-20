from selenium.webdriver.common.by import By
import time
from pageObjects.TutorLoginPage import LoginPage
from pageObjects.addeventPage import AddEventsPage
from utilities import XLUtils
from utilities.customLogger import LogGen
from utilities.readproperties import ReadConfig

#### Addevent,edit,delete,report,completed event)
class Test_AddEvent:
    loginURL = ReadConfig.getApplicationURL()
    email = ReadConfig.getemail()
    password = ReadConfig.getpassword()
    path = ".//testdata/Tutor addevent.xlsx"
    logger = LogGen.loggen()  # Logger
    XLUtils = "C:\\Users\\yoges\\PycharmProjects\\ilrnu\\utilities\\XLUtils.py"

    def test_addnewEvent(self, setup):
        self.logger.info("******* Starting Test_001_DDT_Add event test **********")
        self.logger.info("******* Starting Login DDT Test **********")
        self.driver = setup
        self.driver.get(self.loginURL)
        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickTutorLoginSubmit()
        self.ep = AddEventsPage(self.driver)
        self.ep.eventtab_clk()
        self.ep.addevent_button()

        self.rows = XLUtils.getRowCount(self.path,'Addevent')
        print("Number of Rows in a Excel:", self.rows)
        lst_status = []

        for r in range(2,self.rows+1):
            self.Eventmode = XLUtils.readData(self.path,'Addevent', r, 1)
            self.Eventcategory = XLUtils.readData(self.path,'Addevent', r, 2)
            self.Eventname = XLUtils.readData(self.path,'Addevent', r, 3)
            self.Eventdescription = XLUtils.readData(self.path,'Addevent', r, 4)
            self.Eventaddress = XLUtils.readData(self.path,'Addevent', r, 5)
            self.Eventdate = XLUtils.readData(self.path,'Addevent', r, 6)
            self.EStarttime_hour = XLUtils.readData(self.path,'Addevent', r, 7)
            self.EStarttime_min = XLUtils.readData(self.path,'Addevent', r, 8)
            self.EEndtimehour = XLUtils.readData(self.path,'Addevent', r, 9)
            self.EEndtimemin = XLUtils.readData(self.path,'Addevent', r, 10)
            self.AMPM = XLUtils.readData(self.path,'Addevent', r, 11)
            self.Picture = XLUtils.readData(self.path,'Addevent', r, 12)
            self.Expected = XLUtils.readData(self.path,'Addevent', r, 13)

            self.ep.eventname_txtbox(self.Eventname)
            # Find Top Frame
            # top_frame1 = self.driver.find_element(By.XPATH, self.top_frame1)
            # # Switch to top Frame
            # self.driver.switch_to.frame(top_frame1)
            # # edit tinymce frame
            # mce_edit1 = self.driver.find_element(By.XPATH, self.mce_edit1)
            # # Switch to mce_frame
            # mce_edit1.clear()
            # self.ep.mce_edit(self.Eventdescription)
            # Back to Parent frame
            # self.driver.switch_to.default_content()
            self.ep.eventpic(self.Picture)
            self.ep.eventdate(self.Eventdate)
            self.ep.eventstarttime()
            self.ep.Hourstarttime(self.EStarttimehour)
            self.ep.Minstarttime(self.EStarttimemin)
            self.ep.StartAMPM(self.AMPM)
            self.ep.eventendtime()
            self.ep.Hourendtime(self.EEndtimehour)
            self.ep.Minendtime(self.EEndtimemin)
            self.ep.EndAMPM(self.AMPM)
            time.sleep(5)

            act_title = self.driver.title
            Expected_title = "Events page | @iLRNU"

            if act_title == Expected_title:
                if self.exp == "Pass":
                    self.lp.tutor_logout();

# add events
# Edit events
# delete events
# report events
# publish events
# join event
