from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class AddSubjectPage:
    # Add Subject in My Home page
    addsubjecthomepage = "//div[text()='Add Subject']"

    # Add Subject in tutoring page
    addsubject_tutoringpage = "//div[@id='add-subject-cta-btn']"

    # Tutoring Tab
    tutoringtab = "//h2[@id='tutor-top-nav']"

    # Textbox - XPATH Tutoring - Subject Information page

    subjectname = "//input[@placeholder='Enter your subject name']"
    attend = "//input[@placeholder='eg beginner, 10th standard ']"
    tags = "//input[@class='w-full px-2 text-sm focus:outline-none ']"
    individualprice = "//input[@placeholder='e.g: 500']"
    groupprice = "//input[@placeholder='e.g: 300']"

    # iFrame - XPATH Tutoring - Subject Information page
    subjectdescription_topframe = "(//iframe[@title='Rich Text Area'])[1]"
    subjectdescription_mceedit = "//body[@data-mce-placeholder='Write your subject description must be minimum of 30 words and maximum of 200 words']"
    subjecthighlights_topframe1 = "(//iframe[@title='Rich Text Area'])[2]"
    subjectdescription_mceedit1 = "//body[@data-mce-placeholder='Write the subject highlights/modules point wise, must be minimum of 15 words and maximum of 100 words']"

    # Picture XPATH Tutoring - Subject Information page
    subjectpicture = "//input[@id='event-images']"
    picture = "P:\\iLRNU application\\Testdata\\Maths.jpg"

    # Button -Tutoring - Subject Information page
    save = "//button[normalize-space()='Save']"
    preview = "//button[normalize-space()='Preview']"
    submitsubject = "//button[@class='btn btn-bg-green focus:outline-none']"
    backbutton = "//span[@class='hidden text-sm font-bold lg:text-base lg:flex']"

    # Dropdown XPATH -Tutoring - Subject Information page
    availabilitydays = "(//div[contains(@class,'border rounded-lg border-border_inputs undefined')])[1]"
    # actions = ActionChains(self.driver)
    # actions.move_to_element(availability).perform()
    sunday = "(//label[@for='sunday-availability'])[1]"
    monday = "(//label[@for='monday-availability-1'])[1]"
    tuesday = "(//label[@for='tuesday-availability-2'])[1]"
    wednesday = "(//label[@for='wednesday-availability-3'])[1]"
    thursday = "(//label[@for='thursday-availability-4'])[1]"
    friday = "(//label[@for='friday-availability-5'])[1]"
    saturaday = "(//label[@for='saturday-availability-6'])[1]"

    availabilitytime = "//h2[@class='mb-2 text-base font-bold is-imp']"
    # actions = ActionChains(self.driver)
    # actions.move_to_element(availability1).perform()

    # Index 0 XPATH - SUNDAY Start time selection
    index0StartClick = "(//input[@id='sunday-0-3'])[1]"
    index0Starttimehour = "(//input[@aria-label='Hour'])[1]"
    index0Starttimemin = "(//input[@aria-label='Minute'])[1]"
    index0StartAMPM = "(//span[@title='Click to toggle'][normalize-space()='PM'])[1]"

    # Index 0 XPATH - SUNDAY End time selection
    index0EndClick = "(//input[@id='sunday-0-4'])[1]"
    index0EndtimeHour = "(//input[@aria-label='Hour'])[2]"
    index0EndtimeMin = "(//input[@aria-label='Minute'])[2]"
    index0EndAMPM = "(//span[@title='Click to toggle'][normalize-space()='PM'])[1]"

    # index=1 XPATH - MONDAY Start time selection
    index1StartClick = "(//input[@id='monday-1-3'])[1]"
    index1StarttimeHour = "(//input[contains(@aria-label,'Hour')])[3]"
    index1StarttimeMin = "(//input[contains(@aria-label,'Minute')])[3]"
    index1StartAMPM = "/html[1]/body[1]/div[12]/div[1]/span[2]"

    # index=1 XPATH - MONDAY End time selection
    index1EndClick = "(//input[@id='monday-1-4'])[1]"
    index1EndtimeHour = "(//input[contains(@aria-label,'Hour')])[4]"
    index1EndtimeMin = "(//input[contains(@aria-label,'Minute')])[4]"
    index1EndAMPM = "/html[1]/body[1]/div[13]/div[1]/span[2]"

    # index=2 XPATH -  TUESDAY Start time selection
    index2StartClick = "(//label[@for='tuesday-2-3'])[1]"
    index2StarttimeHour = "(//input[contains(@aria-label,'Hour')])[5]"
    index2StarttimeMin = "(//input[contains(@aria-label,'Minute')])[5]"
    index2StartAMPM = "/html[1]/body[1]/div[16]/div[1]/span[2]"

    # index=2 XPATH -  TUESDAY End time selection
    index2EndClick = "(//input[@id='tuesday-2-4'])[1]"
    index2EndtimeHour = "(//input[contains(@aria-label,'Hour')])[6]"
    index2EndtimeMin = "(//input[contains(@aria-label,'Minute')])[6]"
    index2EndAMPM = "/html[1]/body[1]/div[17]/div[1]/span[2]"

    # index=3 XPATH - WEDNESDAY Start time selection
    index3StartClick = "(//input[@id='wednesday-3-3'])[1]"
    index3StarttimeHour = "(//input[contains(@aria-label,'Hour')])[7]"
    index3StarttimeMin = "(//input[contains(@aria-label,'Minute')])[7]"
    index3StartAMPM = "/html[1]/body[1]/div[20]/div[1]/span[2]"

    # index=3 XPATH - WEDNESDAY End time selection

    index3EndClick = "(//input[@id='wednesday-3-4'])[1]"
    index3EndtimeHour = "(//input[contains(@aria-label,'Hour')])[8]"
    index3EndtimeMin = "(//input[contains(@aria-label,'Minute')])[8]"
    index3EndAMPM = "/html[1]/body[1]/div[21]/div[1]/span[2]"

    # index=4 XPATH - THURSDAY Start time selection
    index4StartClick = "(//label[@for='thursday-4-3'])[1]"
    index4StarttimeHour = "(//input[contains(@aria-label,'Hour')])[9]"
    index4StarttimeMin = "(//input[contains(@aria-label,'Minute')])[9]"
    index4StartAMPM = "/html[1]/body[1]/div[24]/div[1]/span[2]"

    # index=4 XPATH - THURSDAY End time selection
    index4EndClick = "(//input[@id='thursday-4-4'])[1]"
    index4EndtimeHour = "(//input[contains(@aria-label,'Hour')])[10]"
    index4EndtimeMin = "(//input[contains(@aria-label,'Minute')])[10]"
    index4EndAMPM = "/html[1]/body[1]/div[25]/div[1]/span[2]"

    # index=5 XPATH - FRIDAY Start time selection
    index5StartClick = "(//input[@id='friday-5-3'])[1]"
    index5StarttimeHour = "(//input[contains(@aria-label,'Hour')])[11]"
    index5StarttimeMin = "(//input[contains(@aria-label,'Minute')])[11]"
    index5StartAMPM = "/html[1]/body[1]/div[28]/div[1]/span[2]"

    # index=5 XPATH - FRIDAY End time selection
    index5EndClick = "(//input[@id='friday-5-4'])[1]"
    index5EndtimeHour = "(//input[contains(@aria-label,'Hour')])[12]"
    index5EndtimeMin = "(//input[contains(@aria-label,'Minute')])[12]"
    index5EndAMPM = "/html[1]/body[1]/div[29]/div[1]/span[2]"

    # index=6 XPATH - SATURDAY Start time selection
    index6StartClick = "(//label[@for='saturday-6-3'])[1]"
    index6StarttimeHour = "(//input[contains(@aria-label,'Hour')])[13]"
    index6StarttimeMin = "(//input[contains(@aria-label,'Minute')])[13]"
    index6StartAMPM = "/html[1]/body[1]/div[32]/div[1]/span[2]"

    # index=6 XPATH - SATURDAY End time selection

    index6EndClick = "(//input[@id='saturday-6-4'])[1]"
    index6EndtimeHour = "(//input[contains(@aria-label,'Hour')])[14]"
    index6EndtimeMin = "(//input[contains(@aria-label,'Minute')])[14]"
    index6EndAMPM = "/html[1]/body[1]/div[33]/div[1]/span[2]"

    Maxsubject = "// b[text() = 'Maximum number of subjects added']"
    Maximumsubadded = "// b[text() = 'Maximum number of subjects added']"

    # Edit Subject
    editsubject = "// p[text() = 'Edit']"

    # Delete Subject
    deletesubject = "(//p[contains(text(),'Delete')])[1]"

    def __init__(self, driver):
        self.driver = driver

    def maxSubject(self):
        if Maxsubject == Maximumsubadded:
            print("You can add a maximum of 5 subjects")
        else:
            addsubject = self.driver.find_element(By.XPATH, "//div[@id='add-subject-cta-btn']").click()

    def clickaddSubject(self):
        self.driver.find_element(By.XPATH, self.addsubjecthomepage).click()

    def getSubjectName(self):
        return self.driver.find_element(By.XPATH, self.subjectname)

    def enterSubjectName(self, subjectname):
        self.getSubjectName().send_keys(subjectname)

    def getAttend(self):
        return self.driver.find_element(By.XPATH, self.attend)

    def enterAttend(self, attend):
        self.getAttend().send_keys(attend)  # to be clicked to give number of attend

    def getTags(self):
        return self.driver.find_element(By.XPATH, self.tags)

    def enterTags(self, tags):
        self.getTags().send_keys(tags)  # to be clicked to give number of tags

    def getIndividualPrice(self):
        return self.driver.find_element(By.XPATH, self.individualprice)

    def enterIndividualPrice(self, individualprice):
        self.getIndividualPrice().send_keys(individualprice)

    def getGroupPrice(self):
        return self.driver.find_element(By.XPATH, self.groupprice)

    def enterGroupPrice(self, groupprice):
        self.getGroupPrice().send_keys(groupprice)

    def selectFile(self):
        subjectpicture = self.driver.find_element(By.XPATH, self.subjectpicture)
        subjectpicture.send_keys(self.picture)

    # SubjectDescription
    def getTopFrame(self):
        topframe = self.driver.find_element(By.XPATH, self.subjectdescription_topframe)
        self.driver.switch_to.frame(topframe)

    def getMceEdit(self, subjectdescription):
        mce_edit1 = self.driver.find_element(By.XPATH, self.subjectdescription_mceedit)
        mce_edit1.clear()
        mce_edit1.send_keys(subjectdescription)

    def switchToDefault(self):
        self.driver.switch_to.default_content()

    # Subjecthighlight
    def getTopFrame1(self):
        topframe1 = self.driver.find_element(By.XPATH, self.subjecthighlights_topframe1)
        self.driver.switch_to.frame(topframe1)

    def getMceEdit1(self, subjectHighlights):
        mce_edit2 = self.driver.find_element(By.XPATH, self.subjectdescription_mceedit1)
        mce_edit2.clear()
        mce_edit2.send_keys(subjectHighlights)

    def switchToDefault1(self):
        self.driver.switch_to.default_content()

    def selectAvailabilitydays(self):
        # identify element
        availabilitydays = self.driver.find_element(By.XPATH, self.availabilitydays)
        achains = ActionChains(self.driver)
        achains.move_to_element(availabilitydays).perform()
        self.driver.find_element(By.XPATH, self.sunday).click()
        # self.driver.find_element(By.XPATH, self.monday).click()
        # self.driver.find_element(By.XPATH, self.tuesday).click()
        # self.driver.find_element(By.XPATH, self.wednesday).click()
        # self.driver.find_element(By.XPATH, self.thursday).click()
        # self.driver.find_element(By.XPATH, self.friday).click()
        # self.driver.find_element(By.XPATH, self.saturaday).click()

    def startavailabilitytime(self):
        availability = self.driver.find_element(By.XPATH, self.availabilitytime)
        actions = ActionChains(self.driver)
        actions.move_to_element(availability).perform()
        # self.driver.find_element(By.XPATH, self.availabilitytime)
        # self.driver.find_element(By.XPATH, self.index0StartClick).click()
        # self.driver.find_element(By.XPATH, self.index0Starttimehour).send_keys(StarttimeHour)
        # self.driver.find_element(By.XPATH, self.index0Starttimemin).send_keys(StarttimeMin)
        # self.driver.find_element(By.XPATH, self.index0StartAMPM).send_keys(StartAMPM)

    def getStartTime(self):
        return self.driver.find_element(By.XPATH, self.index0StartClick)

    def getHourStartTime(self):
        return self.driver.find_element(By.XPATH, self.index0Starttimehour)

    def getMinStartTime(self):
        return self.driver.find_element(By.XPATH, self.index0Starttimemin)

    def getStartAMPM(self):
        return self.driver.find_element(By.XPATH, self.index0StartAMPM)

    def selectStartTime(self):
        self.getStartTime().click()
        # self.log.info("selected EventStartTime")

    def enterGetHourStartTime(self, StarttimeHour):
        self.getHourStartTime().send_keys(StarttimeHour)
        # self.log.info("Entered Hourstarttime")

    def enterGetMinStartTime(self, StarttimeMin):
        self.getMinStartTime().send_keys(StarttimeMin)
        # self.log.info("Entered Minstarttime")

    def enterStartAMPM(self, StartAMPM):
        self.getStartAMPM().send_keys(StartAMPM)
        # self.log.info("Entered Start_AMPM")

    def endavailabilitytime(self):
        availability1 = self.driver.find_element(By.XPATH, self.availabilitytime)
        actions = ActionChains(self.driver)
        actions.move_to_element(availability1).perform()
        # self.driver.find_element(By.XPATH, self.index0EndClick).click()
        # self.driver.find_element(By.XPATH, self.index0EndtimeHour).send_keys(EndtimeHour)
        # self.driver.find_element(By.XPATH, self.index0EndtimeMin).send_keys(EndtimeMin)
        # self.driver.find_element(By.XPATH, self.index0EndAMPM).send_keys(EndAMPM)

    def getEndTime(self):
        return self.driver.find_element(By.XPATH, self.index0EndClick)

    def getHourEndTime(self):
        return self.driver.find_element(By.XPATH, self.index0EndtimeHour)

    def getMinEndTime(self):
        return self.driver.find_element(By.XPATH, self.index0EndtimeMin)

    def getEndAMPM(self):
        return self.driver.find_element(By.XPATH, self.index0EndAMPM)

    def selectEndTime(self):
        self.getEndTime().click()
        time.sleep(3)
        # self.log.info("selected EventEndTime")

    def enterGetHourEndTime(self, EndtimeHour):
        self.getHourEndTime().send_keys(EndtimeHour)
        # self.log.info("Entered Hourstarttime")

    def enterGetMinEndTime(self, EndtimeMin):
        self.getMinEndTime().send_keys(EndtimeMin)
        # self.log.info("Entered Minstarttime")

    def enterEndAMPM(self, EndAMPM):
        self.getEndAMPM().send_keys(EndAMPM)

    # Index=1
    # self.driver.find_element(By.XPATH, self.index1StartClick).click()
    # self.driver.find_element(By.XPATH, self.index1StarttimeHour).send_keys(StarttimeHour)
    # self.driver.find_element(By.XPATH, self.index1StarttimeMin).send_keys(StarttimeMin)
    # self.driver.find_element(By.XPATH, self.index1StartAMPM).send_keys(StartAMPM)
    # self.driver.find_element(By.XPATH, self.index1EndClick).click()
    # self.driver.find_element(By.XPATH, self.index1EndtimeHour).send_keys(EndtimeHour)
    # self.driver.find_element(By.XPATH, self.index1EndtimeMin).send_keys(EndtimeMin)
    # self.driver.find_element(By.XPATH, self.index1EndAMPM).send_keys(EndAMPM)
    # # Index=2
    # self.driver.find_element(By.XPATH, self.index2StartClick).click()
    # self.driver.find_element(By.XPATH, self.index2StarttimeHour).send_keys(StarttimeHour)
    # self.driver.find_element(By.XPATH, self.index2StarttimeMin).send_keys(StarttimeMin)
    # self.driver.find_element(By.XPATH, self.index2StartAMPM).send_keys(StartAMPM)
    # self.driver.find_element(By.XPATH, self.index2EndClick).click()
    # self.driver.find_element(By.XPATH, self.index2EndtimeHour).send_keys(EndtimeHour)
    # self.driver.find_element(By.XPATH, self.index2EndtimeMin).send_keys(EndtimeMin)
    # self.driver.find_element(By.XPATH, self.index2EndAMPM).send_keys(EndAMPM)
    # # Index=3
    # self.driver.find_element(By.XPATH, self.index3StartClick).click()
    # self.driver.find_element(By.XPATH, self.index3StarttimeHour).send_keys(StarttimeHour)
    # self.driver.find_element(By.XPATH, self.index3StarttimeMin).send_keys(StarttimeMin)
    # self.driver.find_element(By.XPATH, self.index3StartAMPM).send_keys(StartAMPM)
    # self.driver.find_element(By.XPATH, self.index3EndClick).click()
    # self.driver.find_element(By.XPATH, self.index3EndtimeHour).send_keys(EndtimeHour)
    # self.driver.find_element(By.XPATH, self.index3EndtimeMin).send_keys(EndtimeMin)
    # self.driver.find_element(By.XPATH, self.index3EndAMPM).send_keys(EndAMPM)
    # # Index=4
    # self.driver.find_element(By.XPATH, self.index4StartClick).click()
    # self.driver.find_element(By.XPATH, self.index4StarttimeHour).send_keys(StarttimeHour)
    # self.driver.find_element(By.XPATH, self.index4StarttimeMin).send_keys(StarttimeMin)
    # self.driver.find_element(By.XPATH, self.index4StartAMPM).send_keys(StartAMPM)
    # self.driver.find_element(By.XPATH, self.index4EndClick).click()
    # self.driver.find_element(By.XPATH, self.index4EndtimeHour).send_keys(EndtimeHour)
    # self.driver.find_element(By.XPATH, self.index4EndtimeMin).send_keys(EndtimeMin)
    # self.driver.find_element(By.XPATH, self.index4EndAMPM).send_keys(EndAMPM)
    # # Index=5
    # self.driver.find_element(By.XPATH, self.index5StartClick).click()
    # self.driver.find_element(By.XPATH, self.index5StarttimeHour).send_keys(StarttimeHour)
    # self.driver.find_element(By.XPATH, self.index5StarttimeMin).send_keys(StarttimeMin)
    # self.driver.find_element(By.XPATH, self.index5StartAMPM).send_keys(StartAMPM)
    # self.driver.find_element(By.XPATH, self.index5EndClick).click()
    # self.driver.find_element(By.XPATH, self.index5EndtimeHour).send_keys(EndtimeHour)
    # self.driver.find_element(By.XPATH, self.index5EndtimeMin).send_keys(EndtimeMin)
    # self.driver.find_element(By.XPATH, self.index5EndAMPM).send_keys(EndAMPM)
    # # Index=6
    # self.driver.find_element(By.XPATH, self.index6StartClick).click()
    # self.driver.find_element(By.XPATH, self.index6StarttimeHour).send_keys(StarttimeHour)
    # self.driver.find_element(By.XPATH, self.index6StarttimeMin).send_keys(StarttimeMin)
    # self.driver.find_element(By.XPATH, self.index6StartAMPM).send_keys(StartAMPM)
    # self.driver.find_element(By.XPATH, self.index6EndClick).click()
    # self.driver.find_element(By.XPATH, self.index6EndtimeHour).send_keys(EndtimeHour)
    # self.driver.find_element(By.XPATH, self.index6EndtimeMin).send_keys(EndtimeMin)
    # self.driver.find_element(By.XPATH, self.index6EndAMPM).send_keys(EndAMPM)

    # update the data

    # Button XPATH

    def saveButton(self):
        self.driver.find_element(By.XPATH, self.save).click()
        time.sleep(5)

    def previewButton(self):
        self.driver.find_element(By.XPATH, self.preview).click()

    def submitSubject(self):
        self.driver.find_element(By.XPATH, self.submitsubject).click()

    def backButton(self):
        self.driver.find_element(By.XPATH, self.backbutton).click()

    # Edit Subject
    def addSubjecttut(self):
        addsubjecttut = self.driver.find_element(By.XPATH, addsubject_tutoringpage).click()

    def editSubject(self):
        editsubject1 = self.driver.find_element(By.XPATH, editsubject).click()

    def tutoringTab(self):
        tutoringtab1 = self.driver.find_element(By.XPATH, tutoringtab).click()

    # Delete Subject
    def deleteSubject(self):
        deletesubject1 = self.driver.find_element(By.XPATH, deletesubject).click()
