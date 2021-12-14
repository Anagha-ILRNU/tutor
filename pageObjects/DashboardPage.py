import pytest
from selenium.webdriver.common.by import By


class DashboardPage:
    # button_XPATH
    addsubject = "//div[@id='add-subject-cta-btn']"
    createopensession = "//div[contains(@class,'px-4 py-2 mx-auto text-center text-white rounded-md cursor-pointer lg:mx-0 text-md lg:min-w-32 lg:w-auto')][normalize-space()='Create Open Session']"
    starttutoring = "//div[contains(text(),'Start Tutoring')]"
    addcourse = "//div[contains(text(),'Add Course')]"

    # edit_XPATH
    editprofile.XPATH = "//a[text()='Edit Profile']"

    # View_XPATH
    viewprofile.XPATH = "//a[@class='px-3 py-1 text-center text-white rounded-md cursor-pointer bg-unnamed_color text-md']"

    # Invite_XPATH
    invitestudent.XPATH = "//button[contains(@class,'flex items-center mt-2 text-xs font-semibold focus:outline-none lg:text-sm text-green_color')]"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def addSubject(self):
        self.driver.find_element(By.XPATH, self.addsubject.click())

    def createOpenSession(self):
        self.driver.find_element(By.XPATH, self.createopensession.click())

    def startTutoring(self):
        self.driver.find_element(By.XPATH, self.starttutoring.click())

    def addCourse(self):
        self.driver.find_element(By.XPATH, self.addcourse.click())

    def editProfile(self):
        self.driver.find_element(By.XPATH, self.editprofile.click())

    def viewProfile(self):
        self.driver.find_element(By.XPATH, self.viewprofile.click())

    # to check Sign Up Link
    # def is_buyplan_link_exist(self):
    #     return self.is_visible(self.buyplan_LINK)
