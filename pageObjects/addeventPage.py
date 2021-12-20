import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class AddEventPage:
    ####### UserProfile_Button_XPATH ###### Repeated function XPATH

    clickuserprofileicon = "//*[name()='svg' and @data-icon='user-circle']"
    clickloginicon = "//p[text()='Log in']"

    ###### Tutor_Login_XPATH ########## Repeated function XPATH

    inputemail = "//input[@placeholder='Your mail id']"
    inputpassword = "//input[@placeholder='Enter password']"
    submitlogin = " //button[@type='submit']"

    ############ Event Tab in Dashboard ###########

    eventtab = 'event-top-nav'

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
    Hourstarttime = "//body[1]/div[5]/div[1]/div[1]/input[1]"
    Minstarttime = "//body/div[5]/div[1]/div[2]/input[1]"
    Start_AMPM = "//body/div[5]/div[1]/span[2]"
    # Event Endtime in Events Tab
    eventendtime = "//input[@placeholder='End Time']"
    Hourendtime = "//body[1]/div[6]/div[1]/div[1]/input[1]"
    Minendtime = "//body[1]/div[6]/div[1]/div[2]/input[1]"
    End_AMPM = "//body[1]/div[6]/div[1]/span[2]"
    #### Event description #####
    # Find Top Frame
    top_frame = "//iframe[@class='tox-edit-area__iframe']"
    mce_edit = "//body[@class='mce-content-body ']"
    eventpic = "//*[@id='event-images']"
    picture = "P:\iLRNU application\Testdata\Maths.jpg"
    eventpubliccheckbox = "//input[@class='w-5 h-5 sm:w-6 sm:h-6']"

    ###### Save-Preview-back- button #####################
    saveevent = "//button[normalize-space()='Save']"
    previewevent = "//button[normalize-space()='Preview']"
    backevent = "//button[normalize-space()='< Back']"
    Publishevent = "//button[text()='Publish']"
    submitevent = "//button[text()='Submit']"

    ######### Action items for Addeventpage  ##########

    def __init__(self, driver):
        self.driver = driver

    def profileIcon(self):
        userprofile_field = self.driver.find_element(By.XPATH, self.clickuserprofileicon)
        userprofile_field.click()
        login_field = self.driver.find_element(By.XPATH, self.clickloginicon)
        login_field.click()

    ###### TutorLogin_Textbox_XPATH ##########

    def tutorlogin(self, email, password):
        inputemail = self.driver.find_element(By.XPATH, "//input[@placeholder='Your mail id']")
        inputemail.send_keys(email)
        inputpassword = self.driver.find_element(By.XPATH, "//input[@placeholder='Enter password']")
        inputpassword.send_keys(password)
        submitlogin = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        submitlogin.click()

    ##### Event Tab_XPATH #########
    def eventtab_clk(self):
        eventtab_click = self.driver.find_element(By.ID, self.eventtab)
        eventtab_click.click()

    ###### Add Event button_XPATH ##########

    def addevent_button(self):
        addevent_button = self.driver.find_element(By.XPATH, self.addevent)
        addevent_button.click()

    # uploadpicture = "P:\Student_iLRNU\Testdata\Maths.jpg"addevent

    ####### Event information ################# ########### Check the scenario for offline ###########

    def event_information(self):
        offline_txtbox = self.driver.find_element(By.XPATH, self.offline)
        offline_txtbox.click()
        online_txtbox = self.driver.find_element(By.XPATH, self.online)
        online_txtbox.click()
        eventcategory_dropdown = self.driver.find_element(By.XPATH, self.eventcategory)
        eventname_txtbox = self.driver.find_element(By.XPATH, self.eventname)
        eventname_txtbox.send_keys(self.eventname)
        event_date = self.driver.find_element(By.XPATH, self.eventdate)
        event_date.click()
        # Event Starttime in Events Tab
        eventstart_time = self.driver.find_element(By.XPATH, self.eventstarttime)
        eventstart_time.click()
        Hourstart_time = self.driver.find_element(By.XPATH, self.Hourstarttime)
        Hourstart_time.send_keys(self.Hourstarttime)
        Minstart_time = self.driver.find_element(By.XPATH, self.Minstarttime)
        Minstart_time.send_keys(self.Minstarttime)
        Start_AMPM = self.driver.find_element(By.XPATH, self.Start_AM)
        Start_AMPM.send_keys(self.eventAMPM)
        # Event Endtime in Events Tab
        eventend_time = self.driver.find_element(By.XPATH, self.eventendtime)
        eventend_time.click()
        Hourend_time = self.driver.find_element(By.XPATH, self.Hourendtime)
        Hourend_time.send_keys(self.Hourendtime)
        Minend_time = self.driver.find_element(By.XPATH, self.Minendtime)
        Minend_time.send_keys(self.Minendtime)
        End_AMPM = self.driver.find_element(By.XPATH, self.End_AM)
        End_AMPM.send_keys(self.eventAMPM)
        #### Event description #####
        # Find Top Frame
        top_frame1 = self.driver.find_element(By.XPATH, self.top_frame)
        # Switch to top Frame
        self.driver.switch_to.frame(top_frame1)
        # edit tinymce frame
        mce_edit1 = self.driver.find_element(By.XPATH, self.mce_edit)
        # Switch to mce_frame
        mce_edit1.clear()
        self.mce_edit.send_keys(self.eventdescription)
        # Back to Parent frame
        self.driver.switch_to.default_content()
        #### Upload picture####
        event_picture = self.driver.find_element(By.XPATH, self.eventpic)
        event_picture.send_keys(self.picture)
        ##### Checkbox Selection #####
        checkbox_eventpublic = self.driver.find_element(By.XPATH, self.eventpubliccheckbox)
        checkbox_eventpublic.click()

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
