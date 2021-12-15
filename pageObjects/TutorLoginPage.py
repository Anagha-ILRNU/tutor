import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPage:
    # icon_XPATH_Login Page
    user_profile = "//*[name()='svg' and @data-icon='user-circle']"
    tutor_login = "//p[text()='Log in']"

    # Textbox_XPATH_Login Page
    email = "//input[@placeholder='Your mail id']"
    password = "//input[@placeholder='Enter password']"

    # Button_XPATH__Login Page
    tutor_login_submit = "//button[@type='submit']"

    # icon_XPATH( after login)_Dashboard page
    user_profile1 = "//img[@class='w-8 h-8 rounded-full xxl:w-full xxl:h-full'] "
    tutor_logout = "//p[text()='Log out']"

    def __init__(self, driver):
        self.driver = driver

    def userProfile(self):
        self.driver.find_element(By.XPATH, self.user_profile.click())

    def tutorLogin(self):
        self.driver.find_element(By.XPATH, self.tutor_login.click())

    def getEmailField(self):
        return self.driver.find_element(By.XPATH,self.email)

    def enterEmail(self,email):
        self.getEmailField().click()
        self.getEmailField().send_keys(email)

    def getPasswordField(self):
        return self.driver.find_element(By.XPATH,self.password)

    def enterPassword(self,password):
        self.getPasswordField().click()
        self.getPasswordField().send_keys(password)

    def gettutorLoginSubmitField(self):
        return self.driver.find_element(By.XPATH,self.tutor_login_submit)

    def entertutorLoginSubmit(self):
        self.gettutorLoginSubmitField().click()
        time.sleep(5)

    def tutorLogout(self):
        self.driver.find_element(By.XPATH, self.tutor_logout.click())




