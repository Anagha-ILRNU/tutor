import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


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

    offlineselected = "//div[contains(@class,'w-4 h-4 rounded-full cursor-pointer focus:outline-none border-4 border-logo_blue bg-white')]"
    onlineselected = "//div[contains(@class,'w-4 h-4 rounded-full cursor-pointer focus:outline-none border-4 border-logo_blue bg-white')]"

    Onlinenonselected = "//div[contains(@class,'w-4 h-4 rounded-full cursor-pointer focus:outline-none border-2 border-gray-300 bg-white')]"
    Offlineonselected = "//div[contains(@class,'w-4 h-4 rounded-full cursor-pointer focus:outline-none border-2 border-gray-300 bg-white')]"

    eventcategory = "//div[normalize-space()='Sports']"
    category = "(//div[@class='capitalize text-gray-500 font-semibold'])[1]"

    eventname = "//input[@placeholder='Enter your event name']"

    # Date selection
    eventdate = "//*[@placeholder='Start Date']"
    getmonth = "//option[text()='December']"
    getyear = "//input[@min='2021']"
    nextmonth = "//span[@class='flatpickr-next-month']//*[name()='svg']"
    alldates = "//div[@class='flatpickr-days']/div[@class='dayContainer']"

    # Event Starttime in Events Tab
    eventstarttime = "//input[@placeholder='Start Time']"
    Hourstarttime = "(//input[@aria-label='Hour'])[1]"
    Minstarttime = "(//input[@aria-label='Minute'])[1]"
    StartAMPM = "(//span[@title='Click to toggle'][normalize-space()='PM'])[1]"
    # Event Endtime in Events Tab
    eventendtime = "//input[@placeholder='End Time']"
    Hourendtime = "(//input[@aria-label='Hour'])[2]"
    Minendtime = "(//input[@aria-label='Minute'])[2]"
    EndAMPM = "(//span[@title='Click to toggle'][normalize-space()='PM'])[2]"

    top_frame = "//iframe[@class='tox-edit-area__iframe']"
    mce_edit = "//body[@class='mce-content-body ']"
    uploadfile = "//input[@id='event-images']"
    Picture = "P:\\iLRNU application\\Testdata\\Maths.jpg"
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

    # def getPicture(self):
    #     return self.driver.find_element(By.XPATH,self.picture)

    def getOnlineRadioButton(self):
        return self.driver.find_element(By.XPATH, self.online)

    def getOffLineRadioButton(self):
        return self.driver.find_element(By.XPATH, self.offline)

    def getEnterNameField(self):
        return self.driver.find_element(By.XPATH, self.eventname)

    def getEventCategory(self):
        # identify element
        category = self.driver.find_element(By.XPATH, self.category)
        achains = ActionChains(self.driver)
        achains.move_to_element(category).perform()
        self.driver.find_element(By.XPATH, self.eventcategory).click()

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

    # Action items

    def getTopFrame(self):
        topframe = self.driver.find_element(By.XPATH, self.top_frame)
        self.driver.switch_to.frame(topframe)

    def getMceEdit(self, eventdescription):
        mce_edit1 = self.driver.find_element(By.XPATH, self.mce_edit)
        mce_edit1.clear()
        mce_edit1.send_keys(eventdescription)
        time.sleep(5)

    def switchToDefault(self):
        self.driver.switch_to.default_content()

    def eventDate(self):
        eventDate = self.driver.find_element(By.XPATH, self.eventdate).click()

    def selectDate(self, eventdate):
        eventdate = self.driver.find_elements(By.XPATH, self.alldates)
        for date in eventdate:
            if date.get_attribute("aria-label") != "January 22, 2022":
                date.click()
                time.sleep(3)
                break

    def selectFile(self):
        file = self.driver.find_element(By.XPATH, self.uploadfile)
        file.send_keys(self.Picture)

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
