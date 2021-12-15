from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


class SubjectPage:
   # Textbox - XPATH Tutoring - Subject Information page
   subjectname = "//input[@placeholder='Enter your subject name']"
   attend = "//input[@placeholder='eg beginner, 10th standard ']"
   tags = "//input[@class='w-full px-2 text-sm focus:outline-none ']"
   individualprice = "//input[@placeholder='eg beginner, 10th standard ']"
   groupprice = "//input[@placeholder='e.g: 300']"

   # iFrame - XPATH Tutoring - Subject Information page
   subjectdescription_topframe = "//iframe[@title='Rich Text Area'])[1]"
   subjectdescription_mceedit = "//body[@class='mce-content-body ']"
   subjecthighlights_topframe1="//iframe[@title='Rich Text Area'])[2]"
   subjectdescription_mceedit1 = "//body[@class='mce-content-body ']"

   # Picture XPATH Tutoring - Subject Information page
   subjectpicture= "//*[@id='event-images']"
   picture = "C:\\Users\\yoges\\PycharmProjects\\ilrnu\\testdata\\Maths.jpg"


    # Button -Tutoring - Subject Information page
   save =  "//button[normalize-space()='Save']"
   preview = "//button[normalize-space()='Preview']"

   # Dropdown -Tutoring - Subject Information page
   availability = self.driver.find_element(By.XPATH,
                                           "(//div[contains(@class,'border rounded-lg border-border_inputs undefined')])[1]")
   actions = ActionChains(self.driver)
   actions.move_to_element(availability).perform()
   sunday = self.driver.find_element(By.XPATH, "(//label[@for='sunday-availability'])[1]").click()
   monday = self.driver.find_element(By.XPATH, "(//label[@for='monday-availability-1'])[1]").click()
   tuesday = self.driver.find_element(By.XPATH, "(//label[@for='tuesday-availability-2'])[1]").click()
   wednesday = self.driver.find_element(By.XPATH, "(//label[@for='wednesday-availability-3'])[1]").click()
   thursday = self.driver.find_element(By.XPATH, "(//label[@for='thursday-availability-4'])[1]").click()
   friday = self.driver.find_element(By.XPATH, "(//label[@for='friday-availability-5'])[1]").click()
   saturaday = self.driver.find_element(By.XPATH, "(//label[@for='saturday-availability-6'])[1]").click()
   availability1 = self.driver.find_element(By.XPATH, "//h2[@class='mb-2 text-base font-bold is-imp']")
   actions = ActionChains(self.driver)
   actions.move_to_element(availability1).perform()
   Index0 = self.driver.find_element(By.XPATH, "(//input[@id='sunday-0-3'])[1]").click()
   Index0 = self.driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Hour')])[1]").send_keys("StarttimeHour")
   Index0 = self.driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Minute')])[1]").send_keys("StarttimeMin")
   Index0 = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[8]/div[1]/span[2]").send_keys("StartAMPM")

   Index0 = self.driver.find_element(By.XPATH, "(//input[@id='sunday-0-4'])[1]").click()
   Index0 = self.driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Hour')])[2]").send_keys("EndtimeHour")
   Index0 = self.driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Minute')])[2]").send_keys("EndtimeMin")
   Index0 = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[9]/div[1]/span[2]").send_keys("EndAMPM")

   # Index=1
   Index1 = self.driver.find_element(By.XPATH, "(//input[@id='monday-1-3'])[1]").click()
   Index1 = self.driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Hour')])[3]").send_keys("StarttimeHour")
   Index1 = self.driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Minute')])[3]").send_keys("StarttimeMin")
   Index1 = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[12]/div[1]/span[2]").send_keys("StartAMPM")

   Index1 = self.driver.find_element(By.XPATH, "(//input[@id='monday-1-4'])[1]").click()
   Index1 = self.driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Hour')])[4]").send_keys("EndtimeHour")
   Index1 = self.driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Minute')])[4]").send_keys("EndtimeMin")
   Index1 = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[13]/div[1]/span[2]").send_keys("EndAMPM")

   # Index=2
   Index2 = self.driver.find_element(By.XPATH, "(//label[@for='tuesday-2-3'])[1]").click()
   Index2 = self.driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Hour')])[5]").send_keys("StarttimeHour")
   Index2 = self.driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Minute')])[5]").send_keys("StarttimeMin")
   Index2 = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[16]/div[1]/span[2]").send_keys("StartAMPM")

   Index2 = self.driver.find_element(By.XPATH, "(//input[@id='tuesday-2-4'])[1]").click()
   Index2 = self.driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Hour')])[6]").send_keys("EndtimeHour")
   Index2 = self.driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Minute')])[6]").send_keys("EndtimeMin")
   Index2 = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[17]/div[1]/span[2]").send_keys("EndAMPM")

   # Index=3
   Index3 = self.driver.find_element(By.XPATH, "(//input[@id='wednesday-3-3'])[1]").click()
   Index3 = self.driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Hour')])[7]").send_keys("StarttimeHour")
   Index3 = self.driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Minute')])[7]").send_keys("StarttimeMin")
   Index3 = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[20]/div[1]/span[2]").send_keys("StartAMPM")

   Index3 = self.driver.find_element(By.XPATH, "(//input[@id='wednesday-3-4'])[1]").click()
   Index3 = self.driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Hour')])[8]").send_keys("EndtimeHour")
   Index3 = self.driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Minute')])[8]").send_keys("EndtimeMin")
   Index3 = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[21]/div[1]/span[2]").send_keys("EndAMPM")

   # Index=4
   Index4 = self.driver.find_element(By.XPATH, "(//label[@for='thursday-4-3'])[1]").click()
   Index4 = self.driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Hour')])[9]").send_keys("StarttimeHour")
   Index4 = self.driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Minute')])[9]").send_keys("StarttimeMin")
   Index4 = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[24]/div[1]/span[2]").send_keys("StartAMPM")

   Index4 = driver.find_element(By.XPATH, "(//input[@id='thursday-4-4'])[1]").click()
   Index4 = driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Hour')])[10]").send_keys("EndtimeHour")
   Index4 = driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Minute')])[10]").send_keys("EndtimeMin")
   Index4 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[25]/div[1]/span[2]").send_keys("EndAMPM")

   # Index=5
   Index5 = driver.find_element(By.XPATH, "(//input[@id='friday-5-3'])[1]").click()
   Index5 = driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Hour')])[11]").send_keys("StarttimeHour")
   Index5 = driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Minute')])[11]").send_keys(
       "StarttimeMin")
   Index5 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[28]/div[1]/span[2]").send_keys("StartAMPM")

   Index5 = driver.find_element(By.XPATH, "(//input[@id='friday-5-4'])[1]").click()
   Index5 = driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Hour')])[12]").send_keys("EndtimeHour")
   Index5 = driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Minute')])[12]").send_keys("EndtimeMin")
   Index5 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[29]/div[1]/span[2]").send_keys("EndAMPM")

   # Index=6
   Index6 = driver.find_element(By.XPATH, "(//label[@for='saturday-6-3'])[1]").click()
   Index6 = driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Hour')])[13]").send_keys("StarttimeHour")
   Index6 = driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Minute')])[13]").send_keys(
       "StarttimeMin")
   Index6 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[32]/div[1]/span[2]").send_keys("StartAMPM")

   Index6 = driver.find_element(By.XPATH, "(//input[@id='saturday-6-4'])[1]").click()
   Index6 = driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Hour')])[14]").send_keys("EndtimeHour")
   Index6 = driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Minute')])[14]").send_keys("EndtimeMin")
   Index6 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[33]/div[1]/span[2]").send_keys("EndAMPM")

   def __init__(self, driver):
       self.driver = driver

    def getSubjectName(self):
        return self.driver.find_element(By.XPATH,self.subjectname)

    def enterSubjectName(self,subjectname):
        self.getSubjectName().send_keys(subjectname)



    def subject_description(self):
        # Iframes for Subject description
        # Find Top Frame
        top_frame = self.driver.find_element(By.XPATH, self.subjectdescription_topframe)
        # //iframe[@class='tox-edit-area__iframe']")

        # Switch to top Frame
        self.driver.switch_to.frame(top_frame)
        # edit tinymce frame
        mce_edit = self.driver.find_element(By.XPATH,self.subjectdescription_mceedit  )

        # Switch to mce_fra
        mce_edit.clear()
        mce_edit.send_keys(subjectdescription)
        # Back to Parent frame
        driver.switch_to.default_content()

    def subject_highlights(self):
        # Iframes SubjectHighlights
        top_frame1 = self.driver.find_element(By.XPATH,self.subjecthighlights_topframe1 )

        # Switch to top Frame
        self.driver.switch_to.frame(top_frame1)
        # edit tinymce frame
        mce_edit1 = self.driver.find_element(By.XPATH, self.subjectdescription_mceedit1)

        # Switch to mce_frame
        mce_edit1.clear()
        mce_edit1.send_keys(subjectHighlights)
        # Back to Parent frame
        self.driver.switch_to.default_content()


    def uploadPicture(self):
       subjectpicture = self.driver.find_element(By.XPATH, self.subjectpicture)
       subjectpicture.send_keys("picture")

    # for x in range(7):
    # Number of days to be selected - Add,remove days and change time
      availability = self.driver.find_element(By.XPATH,
                                       "(//div[contains(@class,'border rounded-lg border-border_inputs undefined')])[1]")
        actions = ActionChains(self.driver)
        actions.move_to_element(availability).perform()
        sunday = self.driver.find_element(By.XPATH, "(//label[@for='sunday-availability'])[1]").click()
        monday = self.driver.find_element(By.XPATH, "(//label[@for='monday-availability-1'])[1]").click()
        tuesday = self.driver.find_element(By.XPATH, "(//label[@for='tuesday-availability-2'])[1]").click()
        wednesday = self.driver.find_element(By.XPATH, "(//label[@for='wednesday-availability-3'])[1]").click()
        thursday = self.driver.find_element(By.XPATH, "(//label[@for='thursday-availability-4'])[1]").click()
        friday = self.driver.find_element(By.XPATH, "(//label[@for='friday-availability-5'])[1]").click()
        saturaday = self.driver.find_element(By.XPATH, "(//label[@for='saturday-availability-6'])[1]").click()

        tags = self.driver.find_element(By.XPATH, "//input[@class='w-full px-2 text-sm focus:outline-none ']").send_keys(
        addtagsself.)  # to be clicked to give number of tags

    # Subject Starttime in Tutoring Tab

    # Index=0
    availability1 = self.driver.find_element(By.XPATH, "//h2[@class='mb-2 text-base font-bold is-imp']")
    actions = ActionChains(self.driver)
    actions.move_to_element(availability1).perform()
    Index0 = self.driver.find_element(By.XPATH, "(//input[@id='sunday-0-3'])[1]").click()
    Index0 = self.driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Hour')])[1]").send_keys("StarttimeHour")
    Index0 = self.driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Minute')])[1]").send_keys("StarttimeMin")
    Index0 = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[8]/div[1]/span[2]").send_keys("StartAMPM")

    Index0 = self.driver.find_element(By.XPATH, "(//input[@id='sunday-0-4'])[1]").click()
    Index0 = self.driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Hour')])[2]").send_keys("EndtimeHour")
    Index0 = self.driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Minute')])[2]").send_keys("EndtimeMin")
    Index0 = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[9]/div[1]/span[2]").send_keys("EndAMPM")

    # Index=1
    Index1 = self.driver.find_element(By.XPATH, "(//input[@id='monday-1-3'])[1]").click()
    Index1 = self.driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Hour')])[3]").send_keys("StarttimeHour")
    Index1 = self.driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Minute')])[3]").send_keys("StarttimeMin")
    Index1 = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[12]/div[1]/span[2]").send_keys("StartAMPM")

    Index1 = self.driver.find_element(By.XPATH, "(//input[@id='monday-1-4'])[1]").click()
    Index1 = self.driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Hour')])[4]").send_keys("EndtimeHour")
    Index1 = self.driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Minute')])[4]").send_keys("EndtimeMin")
    Index1 = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[13]/div[1]/span[2]").send_keys("EndAMPM")

    # Index=2
    Index2 = self.driver.find_element(By.XPATH, "(//label[@for='tuesday-2-3'])[1]").click()
    Index2 = self.driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Hour')])[5]").send_keys("StarttimeHour")
    Index2 = self.driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Minute')])[5]").send_keys("StarttimeMin")
    Index2 = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[16]/div[1]/span[2]").send_keys("StartAMPM")

    Index2 = self.driver.find_element(By.XPATH, "(//input[@id='tuesday-2-4'])[1]").click()
    Index2 = self.driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Hour')])[6]").send_keys("EndtimeHour")
    Index2 = self.driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Minute')])[6]").send_keys("EndtimeMin")
    Index2 = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[17]/div[1]/span[2]").send_keys("EndAMPM")

    # Index=3
    Index3 = self.driver.find_element(By.XPATH, "(//input[@id='wednesday-3-3'])[1]").click()
    Index3 = self.driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Hour')])[7]").send_keys("StarttimeHour")
    Index3 = self.driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Minute')])[7]").send_keys("StarttimeMin")
    Index3 = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[20]/div[1]/span[2]").send_keys("StartAMPM")

    Index3 = self.driver.find_element(By.XPATH, "(//input[@id='wednesday-3-4'])[1]").click()
    Index3 = self.driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Hour')])[8]").send_keys("EndtimeHour")
    Index3 = self.driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Minute')])[8]").send_keys("EndtimeMin")
    Index3 = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[21]/div[1]/span[2]").send_keys("EndAMPM")

    # Index=4
    Index4 = self.driver.find_element(By.XPATH, "(//label[@for='thursday-4-3'])[1]").click()
    Index4 = self.driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Hour')])[9]").send_keys("StarttimeHour")
    Index4 = self.driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Minute')])[9]").send_keys("StarttimeMin")
    Index4 = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[24]/div[1]/span[2]").send_keys("StartAMPM")

    Index4 = driver.find_element(By.XPATH, "(//input[@id='thursday-4-4'])[1]").click()
    Index4 = driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Hour')])[10]").send_keys("EndtimeHour")
    Index4 = driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Minute')])[10]").send_keys("EndtimeMin")
    Index4 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[25]/div[1]/span[2]").send_keys("EndAMPM")

    # Index=5
    Index5 = driver.find_element(By.XPATH, "(//input[@id='friday-5-3'])[1]").click()
    Index5 = driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Hour')])[11]").send_keys("StarttimeHour")
    Index5 = driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Minute')])[11]").send_keys(
        "StarttimeMin")
    Index5 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[28]/div[1]/span[2]").send_keys("StartAMPM")

    Index5 = driver.find_element(By.XPATH, "(//input[@id='friday-5-4'])[1]").click()
    Index5 = driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Hour')])[12]").send_keys("EndtimeHour")
    Index5 = driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Minute')])[12]").send_keys("EndtimeMin")
    Index5 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[29]/div[1]/span[2]").send_keys("EndAMPM")

    # Index=6
    Index6 = driver.find_element(By.XPATH, "(//label[@for='saturday-6-3'])[1]").click()
    Index6 = driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Hour')])[13]").send_keys("StarttimeHour")
    Index6 = driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Minute')])[13]").send_keys(
        "StarttimeMin")
    Index6 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[32]/div[1]/span[2]").send_keys("StartAMPM")

    Index6 = driver.find_element(By.XPATH, "(//input[@id='saturday-6-4'])[1]").click()
    Index6 = driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Hour')])[14]").send_keys("EndtimeHour")
    Index6 = driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Minute')])[14]").send_keys("EndtimeMin")
    Index6 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[33]/div[1]/span[2]").send_keys("EndAMPM")


    # update the data

    attend = self.driver.find_element(By.XPATH, self.attend).send_keys(attend)  # to be clicked to give number of attend
    individualprice = driver.find_element(By.XPATH, "//input[@placeholder='e.g: 500']").send_keys(500)
    groupprice = driver.find_element(By.XPATH, "//input[@placeholder='e.g: 300']").send_keys(1000)
    save = driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
    preview = driver.find_element(By.XPATH, "//button[normalize-space()='Preview']").click()
