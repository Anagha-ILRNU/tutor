import time

from selenium.webdriver.common.by import By
from pageObjects.TutorLoginPage import LoginPage
from pageObjects.addsubjectPage import AddSubjectPage
from utilities import XLUtils
from utilities.readproperties import ReadConfig


#### Addsubject,edit,delete
class Test_AddSubject:
    loginURL = ReadConfig.getApplicationURL()
    email = ReadConfig.getemail()
    password = ReadConfig.getpassword()
    path = "testdata/Tutor addsubject.xlsx"

    # logger = LogGen.loggen()
    XLUtils = "C:\\Users\\yoges\\PycharmProjects\\ilrnu\\utilities\\XLUtils.py"

    def test_addnewSubject(self, setup):
        # self.logger.info("******* Starting Test_001_DDT_Add event test **********")
        # self.logger.info("******* Starting Login DDT Test **********")
        # Validate the Title and Subject added - Tutor
        self.driver = setup
        self.driver.get(self.loginURL)
        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickTutorLoginSubmit()
        self.subjpage = AddSubjectPage(self.driver)
        self.subjpage.clickaddSubject()

        self.rows = XLUtils.getRowCount(self.path, 'Addsubject')
        print("Number of Rows in a Excel:", self.rows)
        lst_status = []

        for r in range(2, self.rows + 1):
            self.Subjectname = XLUtils.readData(self.path, 'Addsubject', r, 1)
            self.Subjectdescription = XLUtils.readData(self.path, 'Addsubject', r, 2)
            self.Attend = XLUtils.readData(self.path, 'Addsubject', r, 3)
            self.Subjecthighlights = XLUtils.readData(self.path, 'Addsubject', r, 4)
            self.Addtags = XLUtils.readData(self.path, 'Addsubject', r, 5)
            self.Sunday = XLUtils.readData(self.path, 'Addsubject', r, 6)
            self.Monday = XLUtils.readData(self.path, 'Addsubject', r, 7)
            self.Tuesday = XLUtils.readData(self.path, 'Addsubject', r, 8)
            self.Wednesday = XLUtils.readData(self.path, 'Addsubject', r, 9)
            self.Thursday = XLUtils.readData(self.path, 'Addsubject', r, 10)
            self.Friday = XLUtils.readData(self.path, 'Addsubject', r, 11)
            self.Saturday = XLUtils.readData(self.path, 'Addsubject', r, 12)
            self.StarttimeHour = XLUtils.readData(self.path, 'Addsubject', r, 13)
            self.StarttimeMin = XLUtils.readData(self.path, 'Addsubject', r, 14)
            self.EndtimeHour = XLUtils.readData(self.path, 'Addsubject', r, 15)
            self.EndtimeMin = XLUtils.readData(self.path, 'Addsubject', r, 16)
            self.StartAMPM = XLUtils.readData(self.path, 'Addsubject', r, 17)
            self.EndAMPM = XLUtils.readData(self.path, 'Addsubject', r, 18)
            self.Individualprice = XLUtils.readData(self.path, 'Addsubject', r, 19)
            self.Groupprice = XLUtils.readData(self.path, 'Addsubject', r, 20)

            # Subject Information details
            self.subjpage.enterSubjectName(self.Subjectname)
            # self.ep.switchTopFrame() for Subjectdescription
            self.subjpage.getTopFrame()
            self.subjpage.getMceEdit(self.Subjectdescription)
            self.subjpage.switchToDefault()

            self.subjpage.enterAttend(self.Attend)

            self.subjpage.enterIndividualPrice(self.Individualprice)
            self.subjpage.enterGroupPrice(self.Groupprice)
            self.subjpage.selectFile()
            # self.ep.switchTopFrame() for Subjecthighlights
            self.subjpage.getTopFrame1()
            self.subjpage.getMceEdit1(self.Subjecthighlights)
            self.subjpage.switchToDefault1()
            self.subjpage.enterTags(self.Addtags)
            self.subjpage.selectAvailabilitydays()

            # Availability starttime
            self.subjpage.startavailabilitytime()
            self.subjpage.selectStartTime()
            self.subjpage.enterGetHourStartTime(self.StarttimeHour)
            self.subjpage.enterGetMinStartTime(self.StarttimeMin)
            time.sleep(2)
            self.subjpage.enterStartAMPM(self.StartAMPM)

            # Availability endtime
            self.subjpage.endavailabilitytime()
            self.subjpage.selectEndTime()
            self.subjpage.enterGetHourEndTime(self.EndtimeHour)
            self.subjpage.enterGetMinEndTime(self.EndtimeMin)
            self.subjpage.enterEndAMPM(self.EndAMPM)

            # self.subjpage.monday()
            # self.subjpage.tuesday()
            # self.subjpage.wednesday()
            # self.subjpage.thursday()
            # self.subjpage.friday()
            # self.subjpage.saturaday()

            self.subjpage.saveButton()
            self.subjpage.previewButton()
            self.subjpage.submitSubject()

            act_title = self.driver.title
            Expected_title = "Tutors page | @iLRNU"
            result = []
            if act_title == Expected_title:
                assert True
                print("Subject added")
                self.driver.save_screenshot("Screenshots\\" + "subject added.png")
                result.append("Subject added")
                home = self.driver.find_element(By.XPATH, "(//div[contains(text(),'My Home')])[1]").click()
                self.driver.close()
                # addsubject = self.driver.find_element(By.XPATH, "//div[@id='add-subject-cta-btn']").click()
                # gotoSubject = self.driver.find_element(By.XPATH, "//div[@class='self-end hidden mb-2 xl:flex']//button[@class='whitespace-no-wrap btn btn-bg-blue'][normalize-space()='Go to Subjects']").click()
                # addsubject = self.driver.find_element(By.XPATH,"(//button[normalize-space()='Add Subject'])[1]").click()
            else:
                print("Mandatory data not entered")
                self.driver.save_screenshot("Screenshots\\" + "Maximum subject added.png")
                result.append("Mandatory data not entered")
                addsubject = self.driver.find_element(By.XPATH, "//div[@id='add-subject-cta-btn']").is_enabled()
                self.driver.close()
                result = [r, "result"]
                self.result = XLUtils.writeData(self.path, 'Addsubject', r, 21, result)

    # def test_editSubject(self, setup):
    #     # self.logger.info("******* Starting Test_002_DDT_Add event test **********")
    #     # self.logger.info("******* Starting Login DDT Test **********")
    #     #  Edit Subject added - Tutor
    #     self.driver = setup
    #     self.driver.get(self.loginURL)
    #     self.lp = LoginPage(self.driver)
    #     self.lp.setEmail(self.email)
    #     self.lp.setPassword(self.password)
    #     self.lp.clickTutorLoginSubmit()
    #     self.subjpage = AddSubjectPage(self.driver)
    #     self.subjpage.tutoringtab()
    #     self.subjpage.addSubjecttut()
    #     self.subjpage.editsubject()
    #
    #     self.rows = XLUtils.getRowCount(self.path, 'Editsubject')
    #     print("Number of Rows in a Excel:", self.rows)
    #     lst_status = []
    #
    #     for r in range(2, self.rows + 1):
    #         self.Subjectname = XLUtils.readData(self.path, 'Editsubject', r, 1)
    #         self.Subjectdescription = XLUtils.readData(self.path, 'Editsubject', r, 2)
    #         self.Attend = XLUtils.readData(self.path, 'Editsubject', r, 3)
    #         self.Subjecthighlights = XLUtils.readData(self.path, 'Editsubject', r, 4)
    #         self.Addtags = XLUtils.readData(self.path, 'Editsubject', r, 5)
    #         self.availabilitydays = XLUtils.readData(self.path, 'Editsubject', r, 6)
    #         self.Monday = XLUtils.readData(self.path, 'Editsubject', r, 7)
    #         self.Tuesday = XLUtils.readData(self.path, 'Editsubject', r, 8)
    #         self.Wednesday = XLUtils.readData(self.path, 'Editsubject', r, 9)
    #         self.Thursday = XLUtils.readData(self.path, 'Editsubject', r, 10)
    #         self.Friday = XLUtils.readData(self.path, 'Editsubject', r, 11)
    #         self.Saturday = XLUtils.readData(self.path, 'Editsubject', r, 12)
    #         self.StarttimeHour = XLUtils.readData(self.path, 'Editsubject', r, 13)
    #         self.StarttimeMin = XLUtils.readData(self.path, 'Editsubject', r, 14)
    #         self.EndtimeHour = XLUtils.readData(self.path, 'Editsubject', r, 15)
    #         self.EndtimeMin = XLUtils.readData(self.path, 'Editsubject', r, 16)
    #         self.StartAMPM = XLUtils.readData(self.path, 'Editsubject', r, 17)
    #         self.EndAMPM = XLUtils.readData(self.path, 'Editsubject', r, 18)
    #         self.Individualprice = XLUtils.readData(self.path, 'Editsubject', r, 19)
    #         self.Groupprice = XLUtils.readData(self.path, 'Editsubject', r, 20)
    #
    #         # addsubject = self.driver.find_element(By.XPATH, "//div[@id='add-subject-cta-btn']").click()
    #         self.subjpage.enterSubjectName(self.Subjectname)
    #         # self.ep.switchTopFrame() for Subjectdescription
    #         self.subjpage.getTopFrame()
    #         self.subjpage.getMceEdit(self.Subjectdescription)
    #         self.subjpage.switchToDefault()
    #
    #         self.subjpage.enterAttend(self.Attend)
    #
    #         self.subjpage.enterIndividualPrice(self.Individualprice)
    #         self.subjpage.enterGroupPrice(self.Groupprice)
    #         self.subjpage.selectFile()
    #         # self.ep.switchTopFrame() for Subjecthighlights
    #         self.subjpage.getTopFrame1()
    #         self.subjpage.getMceEdit1(self.Subjecthighlights)
    #         self.subjpage.switchToDefault1()
    #         self.subjpage.selectAvailabilitydays(self.availabilitydays)
    #         self.subjpage.enterTags(self.Addtags)
    #         self.subjpage.startavailabilitytime(self.StarttimeHour)
    #         self.subjpage.startavailabilitytime(self.StarttimeMin)
    #         self.subjpage.startavailabilitytime(self.StartAMPM)
    #         self.subjpage.endavailabilitytime(self.EndtimeHour)
    #         self.subjpage.endavailabilitytime(self.EndtimeMin)
    #         self.subjpage.endavailabilitytime(self.EndAMPM)
    #
    #         # self.subjpage.monday()
    #         # self.subjpage.tuesday()
    #         # self.subjpage.wednesday()
    #         # self.subjpage.thursday()
    #         # self.subjpage.friday()
    #         # self.subjpage.saturaday()
    #
    #         self.subjpage.saveButton()
    #         self.subjpage.previewButton()
    #         self.subjpage.submitSubject()
    #
    #         act_title = self.driver.title
    #         Expected_title = "Tutors page | @iLRNU"
    #         result = []
    #         if act_title == Expected_title:
    #             print("Subject edited")
    #             self.driver.save_screenshot("Screenshots\\" + "subject edited.png")
    #             result.append("Subject edited")
    #             self.driver.close()
    #             # home = self.driver.find_element(By.XPATH, "(//div[contains(text(),'My Home')])[1]").click()
    #             # addsubject = self.driver.find_element(By.XPATH, "//div[@id='add-subject-cta-btn']").click()
    #             # gotoSubject = self.driver.find_element(By.XPATH, "//div[@class='self-end hidden mb-2 xl:flex']//button[@class='whitespace-no-wrap btn btn-bg-blue'][normalize-space()='Go to Subjects']").click()
    #             # addsubject = self.driver.find_element(By.XPATH,"(//button[normalize-space()='Add Subject'])[1]").click()
    #         else:
    #             print("subject edited")
    #             self.driver.save_screenshot("Screenshots\\" + "edited subject.png")
    #             result.append("subject edited")
    #             self.driver.close()
    #             # addsubject = self.driver.find_element(By.XPATH, "//div[@id='add-subject-cta-btn']").is_enabled()
    #
    #             result = [r, "result"]
    #             self.result = XLUtils.writeData(self.path, 'Editsubject', r, 21, result)
    #
    # def test_deleteSubject(self, setup):
    #     # self.logger.info("******* Starting Test_002_DDT_Add event test **********")
    #     # self.logger.info("******* Starting Login DDT Test **********")
    #     #  Edit Subject added - Tutor
    #     self.driver = setup
    #     self.driver.get(self.loginURL)
    #     self.lp = LoginPage(self.driver)
    #     self.lp.setEmail(self.email)
    #     self.lp.setPassword(self.password)
    #     self.lp.clickTutorLoginSubmit()
    #     self.subjpage = AddSubjectPage(self.driver)
    #     self.subjpage.tutoringtab()
    #     self.subjpage.addSubjecttut()
    #     self.subjpage.deleteSubject()
    #
    #     act_title = self.driver.title
    #     Expected_title = "Tutors page | @iLRNU"
    #     result = []
    #     if act_title == Expected_title:
    #         print("Subject edited")
    #         self.driver.save_screenshot("Screenshots\\" + "subject edited.png")
    #         result.append("Subject edited")
    #         self.driver.close()
    #         # home = self.driver.find_element(By.XPATH, "(//div[contains(text(),'My Home')])[1]").click()
    #         # addsubject = self.driver.find_element(By.XPATH, "//div[@id='add-subject-cta-btn']").click()
    #         # gotoSubject = self.driver.find_element(By.XPATH, "//div[@class='self-end hidden mb-2 xl:flex']//button[@class='whitespace-no-wrap btn btn-bg-blue'][normalize-space()='Go to Subjects']").click()
    #         # addsubject = self.driver.find_element(By.XPATH,"(//button[normalize-space()='Add Subject'])[1]").click()
    #     else:
    #         print("subject edited")
    #         self.driver.save_screenshot("Screenshots\\" + "edited subject.png")
    #         result.append("subject edited")
    #         self.driver.close()
    #         # addsubject = self.driver.find_element(By.XPATH, "//div[@id='add-subject-cta-btn']").is_enabled()


# self.lp.tutor_logout()
# 5subjected = "//p[@class='text-xs text-gray-700 lg:text-base']"
# more than 5 subjects validation
# draft subject by clicking back  button
# Edit Subject
# delete subject
