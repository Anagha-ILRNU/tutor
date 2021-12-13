from selenium.webdriver.common.by import By


class HomePage:
    # Constructors of the homepage class
    def __init__(self, driver):
        self.driver = driver
        self.driver = wait

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
