from utilities import XLutils
from selenium.webdriver.common.by import By
import time
from pageObjects.DashboardPage import DashboardPage
from pageObjects.TutorLoginPage import LoginPage
from pageObjects.addeventPage import AddEventPage


#### Addevent,edit,delete,report,completed event)
class Test_AddEvent:
    loginURL = "https://uat.ilrnu.com/login/"
    path = ".//testdata/Tutor addevent.xlsx"
    email = "yatutor200@gmail.com"
    password = "India@2020"

    def test_addEvent(self, setup):
        self.driver = setup
        self.driver.get(self.loginURL)
        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickTutorLoginSubmit()
        # self.dp = DashboardPage(self.driver)
        self.ep = AddEventPage(self.driver)
        self.ep.eventtab_clk()
        self.ep.addevent_button()
        ############# DDT for addevent ##########
        self.rows = XLutils.getRowCount(self.path, 'Add event')
        print("Number of Rows in a Excel:", self.rows)
        for r in range(2, self.rows + 1):
            self.Event_mode = self.XLUtils.readData(self.path, 'Add event', r, 1)
            self.Event_category = self.XLUtils.readData(self.path, 'Add event', r, 2)
            self.Event_name = self.XLUtils.readData(self.path, 'Add event', r, 3)
            self.Event_description = self.XLUtils.readData(self.path, 'Add event', r, 4)
            self.Event_address = self.XLUtils.readData(self.path, 'Add event', r, 5)
            self.Event_date = self.XLUtils.readData(self.path, 'Add event', r, 6)
            self.EStart_time_hour = self.XLUtils.readData(self.path, 'Add event', r, 7)
            self.EStart_time_min = self.XLUtils.readData(self.path, 'Add event', r, 8)
            self.EEnd_time_hour = self.XLUtils.readData(self.path, 'Add event', r, 9)
            self.EEnd_time_min = self.XLUtils.readData(self.path, 'Add event', r, 10)
            self.AM_PM = self.XLUtils.readData(self.path, 'Add event', r, 11)
            self.Picture = self.XlUtils.readData(self.path, 'Add event', r, 12)
            self.Expected = self.XLUtils.readData(self.path, 'Add event', r, 13)

            self.ep.eventname(self.Event_name)
            # Find Top Frame
            top_frame1 = self.driver.find_element(By.XPATH, self.top_frame)
            # Switch to top Frame
            self.driver.switch_to.frame(top_frame1)
            # edit tinymce frame
            mce_edit1 = self.driver.find_element(By.XPATH, self.mce_edit)
            # Switch to mce_frame
            mce_edit1.clear()
            self.ep.mce_edit(self.Event_description)
            # Back to Parent frame
            self.driver.switch_to.default_content()
            self.ep.eventpic(self.Picture)
            self.ep.eventdate(self.Event_date)
            self.ep.eventstarttime()
            self.ep.Hourstarttime(self.EStart_time_hour)
            self.ep.Minstarttime(self.EStart_time_min)
            self.ep.Start_AMPM(self.AM_PM)
            self.ep.eventendtime()
            self.ep.Hourendtime(self.EEnd_time_hour)
            self.ep.Minendtime(self.EEnd_time_min)
            self.ep.End_AMPM(self.AM_PM)
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
