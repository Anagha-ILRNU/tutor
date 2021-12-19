import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class DashboardPage:
    # button_XPATH
    addsubject = "//div[@id='add-subject-cta-btn']"
    createopensession = "//div[contains(@class,'px-4 py-2 mx-auto text-center text-white rounded-md cursor-pointer lg:mx-0 text-md lg:min-w-32 lg:w-auto')][normalize-space()='Create Open Session']"
    starttutoring = "//div[contains(text(),'Start Tutoring')]"
    addcourse = "//div[contains(text(),'Add Course')]"

    # edit profile button_XPATH
    editprofile = "//a[text()='Edit Profile']"

    ############# edit profile detail textbox_XPATH ###################

    Profile_editpic = "//div[@class='absolute bottom-0 px-3 py-2 rounded-full cursor-pointer right-2 bg-logo_blue']"
    profile_fullname = "//input[@placeholder='Enter your first name']"
    profile_address = "//input[@placeholder='Enter your address']"
    profile_area = "//input[@placeholder='Enter your area']"
    profile_education = "//input[@placeholder='Enter your Education']"
    profile_yearsofexperience = "//input[@placeholder='Enter your years of experience']"
    profile_responsetime = "//input[@placeholder='Enter your response time']"

    ############# profile_detail iFrame_XPATH #############################

    subjectdescription_topframe = "//iframe[@title='Rich Text Area'])[1]"
    subjectdescription_mceedit = "//body[@class='mce-content-body ']"

    profile_biography = ""

    profile_certification = ""
    profile_achievements = ""

    # edit profile button_XPATH
    profile_back = "//button[text()='Cancel']"
    profile_save = "//button[text()='Save']"

    # View_XPATH
    viewprofile = "//a[@class='px-3 py-1 text-center text-white rounded-md cursor-pointer bg-unnamed_color text-md']"

    # Invite_XPATH
    invitestudent = "//button[contains(@class,'flex items-center mt-2 text-xs font-semibold focus:outline-none lg:text-sm text-green_color')]"

    ############## Password & Security ##############

    currentpassword = "//input[@placeholder='Current password']"
    newpassword = "//input[@placeholder='New password']"
    confirmnewpassword = "//input[@placeholder='Confirm password']"
    updatepassword = "//button[text()='Update Password']"
    forgotpassword = "//div[@class='mt-1 text-sm cursor-pointer text-logo_color hover:underline']"

    ############## My address ######################

    Addaddress = "//div[@class='flex flex-col items-center justify-center m-2 border rounded-lg cursor-pointer w-60 h-44']"

    ######### Actions items for Dashboardpage ###############

    def __init__(self, driver):
        self.driver = driver

    def clickSubject(self):
        click_Subject = self.driver.find_element(By.XPATH, self.addsubject)
        click_Subject.click()

    # def clickSubject(self):
    #     self.getSubject().click()
    #     time.sleep(2)

    def clickCreateOpenSession(self):
        click_CreateOpensession = self.driver.find_element(By.XPATH, self.createopensession)
        click_CreateOpensession.click()

    # def getOpenSession(self):
    #     self.getOpenSession().click()
    #     time.sleep(3)

    def clickStartTutoring(self):
        click_StartTutoring = self.driver.find_element(By.XPATH, self.starttutoring)
        click_StartTutoring.click()
        time.sleep(2)

    # def clickStartTutoring(self):
    #     self.getStartTutoring().click()
    #     time.sleep(3)

    def clickCourse(self):
        click_Course = self.driver.find_element(By.XPATH, self.addcourse)
        click_Course.click()
        time.sleep(2)

    # def clickCourse(self):
    #     self.getCourse().click()
    #     time.sleep(3)

    def editProfile(self):
        self.driver.find_element(By.XPATH, self.editprofile).click()
        time.sleep(2)

    def viewProfile(self):
        self.driver.find_element(By.XPATH, self.viewprofile).click()
        time.sleep(2)

    # to check Sign Up Link
    # def is_buyplan_link_exist(self):
    #     return self.is_visible(self.buyplan_LINK)
