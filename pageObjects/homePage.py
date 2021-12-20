from selenium.webdriver.chrome import webdriver


class HomePage:
    homeURL = "https://uat.ilrnu.com/home/"

    # Constructors of the homepage class
    def __init__(self, driver):
        self.driver = driver

    # locators in Home Page Object Repository
    userprofilefield = "//*[name()='svg' and @data-icon='user-circle']"
    loginfield = "//p[text()='Log in']"

    # Page Actions
    def userprofile(self):
        userprofile = self.driver.find_element(By.XPATH, "//*[name()='svg' and @data-icon='user-circle']")
        userprofile.click()

    def loginoption(self):
        loginfield = self.driver.find_element(By.XPATH, "//p[text()='Log in']")
        loginfield.click()


