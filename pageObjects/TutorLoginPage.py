from selenium import webdriver
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

    ######### Actions items for Tutor Login Page ###############

    def __init__(self, driver):
        self.driver = driver

    def userProfile_icon(self):
        self.driver.find_element(By.XPATH, self.user_profile).click()

    def tutorLogin_icon(self):
        self.driver.find_element(By.XPATH, self.tutor_login).click()

    # def getEmail_Field(self):
    #     email_Field = self.driver.find_element(By.XPATH, self.email)
    #     email_Field.click()
    #     # time.sleep(3)

    def setEmail(self, email):
        #time.sleep(3)
        set_Email = self.driver.find_element(By.XPATH, self.email)  # getEmail_Field)
        set_Email.send_keys(email)

    # def getPassword_Field(self):
    #     get_Password = self.driver.find_element(By.XPATH, self.password)
    #     get_Password.click()
    #     # time.sleep(3)

    def setPassword(self, password):
        #time.sleep(3)
        set_Password = self.driver.find_element(By.XPATH, self.password) # getPassword_Field)
        set_Password.send_keys(password)

    def clickTutorLoginSubmit(self):
        self.driver.find_element(By.XPATH, self.tutor_login_submit).click()
        time.sleep(5)

    def userProfile1(self):
        self.driver.find_element(By.XPATH, self.user_profile1).click()
        time.sleep(5)

    def tutorLogout(self):
        self.driver.find_element(By.XPATH, self.tutor_logout).click()
        time.sleep(5)
