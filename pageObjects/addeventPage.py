import time
from selenium.webdriver.common.by import By


class AddEventsPage:
    # log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    # Locators

    ####### UserProfile_Button_XPATH ###### Repeated function XPATH

    clickuserprofileicon = "//*[name()='svg' and @data-icon='user-circle']"
    clickloginicon = "//p[text()='Log in']"

    ###### Tutor_Login_XPATH ########## Repeated function XPATH

    email = "//input[@placeholder='Your mail id']"
    password = "//input[@placeholder='Enter password']"
    submit_button = " //button[@type='submit']"

    ############ Event Tab in Dashboard ###########

    eventtab = "(//h2[normalize-space()='Events'])[1]"

    ########### Add Event Button ################

    addevent = "//button[text()='Add Event']"

    ########### Event information #############

    offline = "//button[text()='Offline']"
    online = "//button[text()='Online']"
    # uploadpicture = "P:\Student_iLRNU\Testdata\Maths.jpg"
    eventcategory = "//div[@class='flex items-center justify-between py-2 px-4  border rounded-lg border-primary py-4 border-gray-400']"
    eventname = "//input[@placeholder='Enter your event name']"
    eventdate = "//*[@placeholder='Start Date']"
    # Event Starttime in Events Tab
    eventstarttime = "//input[@placeholder='Start Time']"
    Hourstarttime = "(//input[@aria-label='Hour'])[1]"
    Minstarttime = "(//input[@aria-label='Minute'])[1]"
    StartAMPM = "(//span[@title='Click to toggle'][normalize-space()='PM'])[1]"
    # Event Endtime in Events Tab
    eventendtime = "//input[@placeholder='End Time']"
    Hourendtime = "//body[1]/div[6]/div[1]/div[1]/input[1]"
    Minendtime = "//body[1]/div[6]/div[1]/div[2]/input[1]"
    EndAMPM = "//body[1]/div[6]/div[1]/span[2]"

    top_frame = "//iframe[@class='tox-edit-area__iframe']"
    mce_edit = "//body[@class='mce-content-body ']"
    eventpic = "(//label[normalize-space()='Select file'])[1]"
    picture = "P:\iLRNU application\Testdata\Maths.jpg"
    eventpubliccheckbox = "//input[@class='w-5 h-5 sm:w-6 sm:h-6']"

    ###### Save-Preview-back- button #####################
    saveevent = "//button[normalize-space()='Save']"
    previewevent = "//button[normalize-space()='Preview']"
    backevent = "//button[normalize-space()='< Back']"
    Publishevent = "//button[text()='Publish']"
    submitevent = "//button[text()='Submit']"

    # Selectors
    def getProfileIcon(self):
        return self.driver.find_element(By.XPATH, self.clickuserprofileicon)

    def getLoginIcon(self):
        return self.driver.find_element(By.XPATH, self.clickloginicon)

    def getEmailField(self):
        return self.driver.find_element(By.XPATH, self.email)

    def getPasswordField(self):
        return self.driver.find_element(By.XPATH, self.password)

    def getLoginButton(self):
        return self.driver.find_element(By.XPATH, self.submit_button)

    def getEventTab(self):
        return self.driver.find_element(By.XPATH, self.eventtab)

    def getAddEventButton(self):
        return self.driver.find_element(By.XPATH, self.addevent)

    def getOnlineRadioButton(self):
        return self.driver.find_element(By.XPATH, self.online)

    def getOffLineRadioButton(self):
        return self.driver.find_element(By.XPATH, self.offline)

    def getEnterNameField(self):
        return self.driver.find_element(By.XPATH, self.eventname)

    def getPictureField(self):
        return self.driver.find_element(By.XPATH, self.eventpic)

    # def uploadPic(self):
    #     return self.driver.find_element(By.XPATH, self.picture)

    def getEventStartTime(self):
        return self.driver.find_element(By.XPATH, self.eventstarttime)

    def getHourStartTime(self):
        return self.driver.find_element(By.XPATH, self.Hourstarttime)

    def getMinStartTime(self):
        return self.driver.find_element(By.XPATH, self.Minstarttime)

    def getStartAMPM(self):
        return self.driver.find_element(By.XPATH, self.StartAMPM)

    def getEventEndTime(self):
        return self.driver.find_element(By.XPATH, self.eventendtime)

    def getHourEndTime(self):
        return self.driver.find_element(By.XPATH, self.Hourendtime)

    def getMinEndTime(self):
        return self.driver.find_element(By.XPATH, self.Minendtime)

    def getEndAMPM(self):
        return self.driver.find_element(By.XPATH, self.EndAMPM)

    def getEventdate(self):
        return self.driver.find_element(By.XPATH, self.eventdate)

    def getPublicCheckbox(self):
        return self.driver.find_element(By.XPATH, self.eventpubliccheckbox)

    def getTopFrame(self):
        topframe = self.driver.find_element(By.XPATH, self.top_frame)
        self.driver.switch_to.frame(topframe)

    # def switchTopFrame(self):
    #     self.driver.switch_to.frame(self.getTopFrame)

    # def setTopFrame(self, top_frame):

    def getMceEdit(self, eventdescription):
        mce_edit1 = self.driver.find_element(By.XPATH, self.mce_edit)
        mce_edit1.clear()
        mce_edit1.send_keys(eventdescription)

        # mce_edit.send_keys(eventdescription)

    # def setMceEdit(self,eventdescription):
    #     mce_edit1.send_keys(eventdescription)
    #     self.driver.switch_to.default_content()

    def switchToDefault(self):
        self.driver.switch_to.default_content()

    def clickProfileIcon(self):
        self.getLoginIcon().click()

    def clickLoginicon(self):
        self.getLoginIcon().click()

    def enterEmail(self, email):
        self.getEmailField.send_keys(email)
        self.log.info("entered email: " + email)

    def enterPassword(self, password):
        self.getPasswordField().send_keys(password)
        self.log.info("entered password: " + password)

    def clickLoginButton(self):
        self.getLoginButton.click()
        self.log.info("clicked on login button")

    def clickEventTab(self):
        self.getEventTab().click()
        # self.log.info("clicked on Event tab")

    def clickAddEventButton(self):
        self.getAddEventButton().click()
        # self.log.info("clicked on Event button")

    ####### Event information ################# ########### Check the scenario for offline ###########
    def selectOnline(self):
        self.getOnlineRadioButton.click()
        # self.log.info("selected online")

    def selectOffline(self):
        self.getoffLineRadioButton.click()
        # self.log.info("selected offline")

    def enterEventName(self, eventname):
        self.getEnterNameField().send_keys(eventname)
        # self.log.info("entered eventname: " + eventname)

    def enterEventDate(self, eventdate):
        self.getEventdate().click()
        # self.getEventdate.send_keys(eventdate)

    def selectEventStartTime(self):
        self.getEventStartTime().click()
        # self.log.info("selected EventStartTime")

    def enterGetHourStartTime(self, Hourstarttime):
        self.getHourStartTime().send_keys(Hourstarttime)
        # self.log.info("Entered Hourstarttime")

    def enterGetMinStartTime(self, Minstarttime):
        self.getMinStartTime().send_keys(Minstarttime)
        # self.log.info("Entered Minstarttime")

    def enterStartAMPM(self, StartAMPM):
        self.getStartAMPM().send_keys(StartAMPM)
        # self.log.info("Entered Start_AMPM")

    def selectEventEndTime(self):
        self.getEventEndTime().click()
        # self.log.info("selected EventEndTime")

    def enterGetHourEndTime(self, Hourendtime):
        self.getHourEndTime().send_keys(Hourendtime)
        # self.log.info("Entered Hourstarttime")

    def enterGetMinEndTime(self, Minendtime):
        self.getMinEndTime().send_keys(Minendtime)
        # self.log.info("Entered Minstarttime")

    def enterEndAMPM(self, EndAMPM):
        self.getEndAMPM().send_keys(EndAMPM)
        time.sleep(5)

    def uploadpicture(self, picture):
        self.getPictureField().click()
        self.getPictureField().send_keys(picture)
        # event_picture = self.driver.find_element(By.XPATH, self.eventpic)
        # event_picture.send_keys(self.picture)

    def clickCheckBox(self):
        self.getPublicCheckbox().click()
        # checkbox_eventpublic = self.driver.find_element(By.XPATH, self.eventpubliccheckbox)
        # checkbox_eventpublic.click()

    def publish_button(self):
        saveevent_button = self.driver.find_element(By.XPATH, self.saveevent)
        saveevent_button.click()
        time.sleep(5)
        previewevent_button = self.driver.find_element(By.XPATH, self.previewevent)
        previewevent_button.click()
        time.sleep(5)
        back_button = self.driver.find_element(By.XPATH, self.backevent)
        back_button.click()
        time.sleep(5)
        Publish_button = self.driver.find_element(By.XPATH, self.Publishevent)
        Publish_button.click()
        submitevent_button = self.driver.find_element(By.XPATH, self.submitevent)
        submitevent_button.click()
