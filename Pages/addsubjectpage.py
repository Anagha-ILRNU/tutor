# To add subject in home page
from ddt import unpack, data
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager import driver
from Config.configuration import TestData
from utilities.utils import Utils


class SubjectPage:
    def __init__(self, driver):
        super().__init__(driver)
        self.wait = driver.get(TestData.SUBJECT_URL)


    # locators

      subjectname = "//input[@placeholder='Enter your subject name']"
      subjectdescription_topframe = "//iframe[@title='Rich Text Area'])[1]"
      subjectdescription_mceedit = "//body[@class='mce-content-body ']"
      attend="//input[@placeholder='eg beginner, 10th standard ']"
      subjecthighlights_topframe1="//iframe[@title='Rich Text Area'])[2]"
      subjectdescription_mceedit1 = "//body[@class='mce-content-body ']"
      subjectpicture= "//*[@id='event-images']"
      tags = "//input[@class='w-full px-2 text-sm focus:outline-none ']"
      individualprice="//input[@placeholder='eg beginner, 10th standard ']"
      groupprice = "//input[@placeholder='e.g: 300']"
      save =  "//button[normalize-space()='Save']"
      preview = "//button[normalize-space()='Preview']"
      availability =
      availability1=




    def subject_name(self):
        subjectname = self.driver.find_element(By.XPATH, self.submitname).send_keys(subjectname)

    def subject_description(self):
        # Iframes for Subject description
        # Find Top Frame
        top_frame = self.driver.find_element(By.XPATH, self.subjectdescription_topframe)
        # //iframe[@class='tox-edit-area__iframe']")

        # Switch to top Frame
        driver.switch_to.frame(top_frame)
        # edit tinymce frame
        mce_edit = driver.find_element(By.XPATH,self.subjectdescription_mceedit  )

        # Switch to mce_fra
        mce_edit.clear()
        mce_edit.send_keys(subjectdescription)
        # Back to Parent frame
        driver.switch_to.default_content()

    def subject_highlights(self):
        # Iframes SubjectHighlights
        top_frame1 = driver.find_element(By.XPATH,self.subjecthighlights_topframe1 )

        # Switch to top Frame
        driver.switch_to.frame(top_frame1)
        # edit tinymce frame
        mce_edit1 = driver.find_element(By.XPATH, self.subjectdescription_mceedit1)

        # Switch to mce_frame
        mce_edit1.clear()
        mce_edit1.send_keys(subjectHighlights)
        # Back to Parent frame
        driver.switch_to.default_content()

    def subject_picture(self):
        subjectpicture = self.driver.find_element(By.XPATH, self.subjectpicture)
        subjectpicture.send_keys("C:\\Users\\yoges\\PycharmProjects\\ilrnu\\testdata\\Maths.jpg")

    # for x in range(7):
    # Number of days to be selected - Add,remove days and change time
      availability = driver.find_element(By.XPATH,
                                       "(//div[contains(@class,'border rounded-lg border-border_inputs undefined')])[1]")
    actions = ActionChains(driver)
    actions.move_to_element(availability).perform()
    sunday = driver.find_element(By.XPATH, "(//label[@for='sunday-availability'])[1]").click()
    monday = driver.find_element(By.XPATH, "(//label[@for='monday-availability-1'])[1]").click()
    tuesday = driver.find_element(By.XPATH, "(//label[@for='tuesday-availability-2'])[1]").click()
    wednesday = driver.find_element(By.XPATH, "(//label[@for='wednesday-availability-3'])[1]").click()
    thursday = driver.find_element(By.XPATH, "(//label[@for='thursday-availability-4'])[1]").click()
    friday = driver.find_element(By.XPATH, "(//label[@for='friday-availability-5'])[1]").click()
    saturaday = driver.find_element(By.XPATH, "(//label[@for='saturday-availability-6'])[1]").click()

    tags = driver.find_element(By.XPATH, "//input[@class='w-full px-2 text-sm focus:outline-none ']").send_keys(
        addtags)  # to be clicked to give number of tags

    # Subject Starttime in Tutoring Tab

    # Index=0
    availability1 = driver.find_element(By.XPATH, "//h2[@class='mb-2 text-base font-bold is-imp']")
    actions = ActionChains(driver)
    actions.move_to_element(availability1).perform()
    Index0 = driver.find_element(By.XPATH, "(//input[@id='sunday-0-3'])[1]").click()
    Index0 = driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Hour')])[1]").send_keys("StarttimeHour")
    Index0 = driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Minute')])[1]").send_keys("StarttimeMin")
    Index0 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[8]/div[1]/span[2]").send_keys("StartAMPM")

    Index0 = driver.find_element(By.XPATH, "(//input[@id='sunday-0-4'])[1]").click()
    Index0 = driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Hour')])[2]").send_keys("EndtimeHour")
    Index0 = driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Minute')])[2]").send_keys("EndtimeMin")
    Index0 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[9]/div[1]/span[2]").send_keys("EndAMPM")

    # Index=1
    Index1 = driver.find_element(By.XPATH, "(//input[@id='monday-1-3'])[1]").click()
    Index1 = driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Hour')])[3]").send_keys("StarttimeHour")
    Index1 = driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Minute')])[3]").send_keys("StarttimeMin")
    Index1 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[12]/div[1]/span[2]").send_keys("StartAMPM")

    Index1 = driver.find_element(By.XPATH, "(//input[@id='monday-1-4'])[1]").click()
    Index1 = driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Hour')])[4]").send_keys("EndtimeHour")
    Index1 = driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Minute')])[4]").send_keys("EndtimeMin")
    Index1 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[13]/div[1]/span[2]").send_keys("EndAMPM")

    # Index=2
    Index2 = driver.find_element(By.XPATH, "(//label[@for='tuesday-2-3'])[1]").click()
    Index2 = driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Hour')])[5]").send_keys("StarttimeHour")
    Index2 = driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Minute')])[5]").send_keys("StarttimeMin")
    Index2 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[16]/div[1]/span[2]").send_keys("StartAMPM")

    Index2 = driver.find_element(By.XPATH, "(//input[@id='tuesday-2-4'])[1]").click()
    Index2 = driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Hour')])[6]").send_keys("EndtimeHour")
    Index2 = driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Minute')])[6]").send_keys("EndtimeMin")
    Index2 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[17]/div[1]/span[2]").send_keys("EndAMPM")

    # Index=3
    Index3 = driver.find_element(By.XPATH, "(//input[@id='wednesday-3-3'])[1]").click()
    Index3 = driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Hour')])[7]").send_keys("StarttimeHour")
    Index3 = driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Minute')])[7]").send_keys("StarttimeMin")
    Index3 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[20]/div[1]/span[2]").send_keys("StartAMPM")

    Index3 = driver.find_element(By.XPATH, "(//input[@id='wednesday-3-4'])[1]").click()
    Index3 = driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Hour')])[8]").send_keys("EndtimeHour")
    Index3 = driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Minute')])[8]").send_keys("EndtimeMin")
    Index3 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[21]/div[1]/span[2]").send_keys("EndAMPM")

    # Index=4
    Index4 = driver.find_element(By.XPATH, "(//label[@for='thursday-4-3'])[1]").click()
    Index4 = driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Hour')])[9]").send_keys("StarttimeHour")
    Index4 = driver.find_element(By.XPATH, "(//input[contains(@aria-label,'Minute')])[9]").send_keys("StarttimeMin")
    Index4 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[24]/div[1]/span[2]").send_keys("StartAMPM")

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

    attend = driver.find_element(By.XPATH, self.attend).send_keys(
        attend)  # to be clicked to give number of attend
    individualprice = driver.find_element(By.XPATH, "//input[@placeholder='e.g: 500']").send_keys(500)
    groupprice = driver.find_element(By.XPATH, "//input[@placeholder='e.g: 300']").send_keys(1000)
    save = driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
    preview = driver.find_element(By.XPATH, "//button[normalize-space()='Preview']").click()
