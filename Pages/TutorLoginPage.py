from selenium.webdriver.common.by import By

class LoginPage:
    textbox_email_XPATH = "//input[@placeholder='Your mail id']"
    textbox_password_XPATH = "//input[@placeholder='Enter password']"
    button_login_submit_XPATH = "//button[@type='submit']"
    user_profile_XPATH = "//*[name()='svg' and @data-icon='user-circle']"
    tutor_login_XPATH = "//p[text()='Log in']"

    def __init__(self, driver):
        self.driver = driver

    def userProfile(self):
        self.driver.find_element(By.XPATH, self.user_profile_XPATH.click())

    def tutorLogin(self):
        self.driver.find_element(By.XPATH, self.tutor_login_XPATH.click())

    def setEmail(self,email):
        self.driver.find_element(By.XPATH, self.textbox_email_XPATH.clear())
        self.driver.find_element(By.XPATH, self.textbox_email_XPATH.send_keys(email))

    def setPassword(self,password):
        self.driver.find_element(By.XPATH, self.textbox_password_XPATH.clear())
        self.driver.find_element(By.XPATH, self.textbox_password_XPATH.send_keys(password))

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_submit_XPATH.click())


