from Pages.BasePage import BasePage
from ddt import data, unpack
from selenium.webdriver.common.by import By
from Config.configuration import TestData
from Pages.BasePage import BasePage
from utilities.utils import Utils

class DashboardPage(BasePage):

    # Constructors of the page class
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.DASHBOARD_URL)

    # Page Actions """

    # to get Page Title
    def get_dashboard_page_title(self, title):
        return self.get_title(title)

    # to check Sign Up Link
    def is_buyplan_link_exist(self):
        return self.is_visible(self.buyplan_LINK)

    # To Create Session in home page
    @data(*Utils.read_data_from_excel("C:\\Users\\yoges\\PycharmProjects\\ilrnu\\testdata\\Create session.xlsx",
                                      "Create session"))
    @unpack
    def create_session_home_page(self):
        return self.is_visible(self.SIGNUP_LINK)

    # To Start Chart & Tutoring
    def start_tutoring_home_page(self):
        return self.is_visible(self.SIGNUP_LINK)

    # To Add Courses
    def add_courses_home_page(self):
        return self.is_visible(self.SIGNUP_LINK)

    # To view Profile
    def view_profile_home_page(self):
        return self.is_visible(self.SIGNUP_LINK)

    # To Edit Profile in home page
    def edit_profile_home_page(self):
        return self.is_visible(self.SIGNUP_LINK)

