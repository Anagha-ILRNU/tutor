import time
from selenium.webdriver.common.by import By


class DashboardPage:
    # button_XPATH
    addsubject = "//div[@id='add-subject-cta-btn']"
    createopensession = "//div[contains(@class,'px-4 py-2 mx-auto text-center text-white rounded-md cursor-pointer lg:mx-0 text-md lg:min-w-32 lg:w-auto')][normalize-space()='Create Open Session']"
    starttutoring = "//div[contains(text(),'Start Tutoring')]"
    addcourse = "//div[contains(text(),'Add Course')]"

    # edit_XPATH
    editprofile = "//a[text()='Edit Profile']"

    # View_XPATH
    viewprofile = "//a[@class='px-3 py-1 text-center text-white rounded-md cursor-pointer bg-unnamed_color text-md']"

    # Invite_XPATH
    invitestudent = "//button[contains(@class,'flex items-center mt-2 text-xs font-semibold focus:outline-none lg:text-sm text-green_color')]"

    def __init__(self, driver):
        self.driver = driver

    def getSubject(self):
        return self.driver.find_element(By.XPATH,self.addsubject)

    def clickSubject(self):
        self.getSubject().click()
        time.sleep(2)

    def clickCreateOpenSession(self):
        self.driver.find_element(By.XPATH,self.createopensession).click()
        time.sleep(2)

    # def clickCreateOpenSession(self):
    #     self.getCreateOpenSession().click()
    #     time.sleep(3)

    def clickStartTutoring(self):
        self.driver.find_element(By.XPATH,self.starttutoring).click()
        time.sleep(2)

    # def clickStartTutoring(self):
    #     self.getStartTutoring().click()
    #     time.sleep(3)

    def clickCourse(self):
        self.driver.find_element(By.XPATH,self.addcourse).click()
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
