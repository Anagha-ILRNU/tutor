from selenium.webdriver.common.by import By


class payment:
    ########### Summary - KYC ###############
    addkyc = "//div[text()='Add KYC']"

    ########## Add KYC details ##############

    Accountholdername= ""
    Accountnumber= ""
    Confirmaccountnumber= ""
    IFSC code= ""
    cancelledchequepic = ""


    def __init__(self, driver):
        self.driver = driver

    def Addkyc(self):
        self.driver.find_element(By.XPATH, self.addkyc.click())

    def setkyc(self):
        self.driver.find_element(By.XPATH, self.addkyc.click())



