from Pages.BasePage import BasePage

class DashboardPage(BasePage):
    button_addsubject.XPATH = "//div[@id='add-subject-cta-btn']"
    button_createopensession.XPATH = "//div[contains(@class,'px-4 py-2 mx-auto text-center text-white rounded-md cursor-pointer lg:mx-0 text-md lg:min-w-32 lg:w-auto')][normalize-space()='Create Open Session']"
    button_starttutoring.XPATH = "//div[contains(text(),'Start Tutoring')]"
    button_addcourse.XPATH = "//div[contains(text(),'Add Course')]"
    edit_profile.XPATH = "//a[text()='Edit Profile']"
    view_profile.XPATH = "//a[@class='px-3 py-1 text-center text-white rounded-md cursor-pointer bg-unnamed_color text-md']"
    invite_student.XPATH = "//button[contains(@class,'flex items-center mt-2 text-xs font-semibold focus:outline-none lg:text-sm text-green_color')]"








    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

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

