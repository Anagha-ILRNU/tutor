from selenium.webdriver.common.by import By
from Config.configuration import TestData
from Pages.BasePage import BasePage


class LoginPage(BasePage):
    # locators in Login Page Object Repository

    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    LOGIN_SUBMIT = (By.ID, "submit")
    LOGIN_GMAIL = (By.NAME, "Login with gmail")
    SIGNUP_LINK = (By.NAME, "sign up")

    # Constructors of the page class
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    # Page Actions """

    # to get Page Title
    def get_login_page_title(self, title):
        return self.get_title(title)

    # to check Sign Up Link
    def is_signup_link_exist(self):
        return self.is_visible(self.SIGNUP_LINK)

    # to login to app
    def do_login(self, email, password):
        self.do.send_keys(self.EMAIl, TestData.EMAIL)
        self.do.send_keys(self.PASSWORD, TestData.PASSWORD)
        self.do_click(self.LOGIN_BUTTON)
