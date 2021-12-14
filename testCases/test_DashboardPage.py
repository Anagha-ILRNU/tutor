import pytest
from selenium import webdriver
from pageObjects.DashboardPage import DashboardPage


class Test_002_DashBoard:
    #  Pre Condition Buy plan
    # def test_Buy_plan(self):
    #     buyplan = buyplan(self.driver)
    def test_login(self,setup):
    def test_addSubject_Button(self):
        sub = SubjectPage(self.driver)

    def test_createOpenSession(self):
        sub = SubjectPage(self.driver)

    def test_startTutoring(self):
        sub = SubjectPage(self.driver)

    def test_addCourse(self):
        sub = SubjectPage(self.driver)

    def test_editProfile(self):
        sub = SubjectPage(self.driver)

    def test_viewProfile(self):
        sub = SubjectPage(self.driver)


        #Add Subjects
        #Create open session
        #Start tutoring
        #Add course
        #Edit profile
        #view profile
        #invite your student


        # lf.homepage = HomePage(self.driver)
        # title = self.loginpage.get_title(TestData.TUTORPAGE_TITLE)
        # assert title == TestData.TUTORPAGE_TITLE

    # def test_create_session_home_page(self):
    #     self.homepage = HomePage(self.driver)
    #     title = self.loginpage.get_title(TestData.LOGIN_PAGE_TITLE)
    #     assert title == TestData.LOGIN_PAGE_TITLE

    # def start_tutoring_home_page(self):
    #     return self.is_visible(self.SIGNUP_LINK)
    #
    # # To Add Courses
    # def add_courses_home_page(self):
    #     return self.is_visible(self.SIGNUP_LINK)
    #
    # # To view Profile
    # def view_profile_home_page(self):
    #     return self.is_visible(self.SIGNUP_LINK)
    #
    # # To Edit Profile in home page
    # def edit_profile_home_page(self):
    #     return self.is_visible(self.SIGNUP_LINK)

    # def test_login_succesfully(self, Email, Password):
    #     self.loginPage = LoginPage(self.driver)
    #     self.loginpage.do_login()
    #
    # def test_validate_dashboard_title(self):
    #     self.homepage = HomePage(self.driver)
    #     title = self.loginpage.get_title(TestData.DASHBOARD_TITLE)
    #     assert title == TestData.DASHBOARD_TITLE
    #
    # def test_add_subject_enabled(self):
    #     self.homepage = HomePage(self.driver)
    #     flag = self.homepage.is_add_subject.is_enabled()
    #     assert flag
