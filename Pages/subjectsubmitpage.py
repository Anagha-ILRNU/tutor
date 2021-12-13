from selenium.webdriver.common.by import By


class SubmitResult:
    def __init__(self,driver):
        self.driver = driver

    # Locators

    SUBMIT_SUBJECT = "//button[@class='btn btn-bg-green focus:outline-none']"

    def submit_subject(self):
        Subjectsubmit = self.driver.find_element(By.XPATH, self.SUBMIT_SUBJECT).click()


