import time
from pageObjects.TutorLoginPage import LoginPage
from pageObjects.addsubjectPage import AddSubjectPage
from utilities import XLUtils
from utilities.readproperties import ReadConfig


#### Addevent,edit,delete,report,completed event)
class Test_AddEvent:
    loginURL = ReadConfig.getApplicationURL()
    email = ReadConfig.getemail()
    password = ReadConfig.getpassword()
    path = "testdata/Tutor addsubject.xlsx"
    # logger = LogGen.loggen()
    XLUtils = "C:\\Users\\yoges\\PycharmProjects\\ilrnu\\utilities\\XLUtils.py"

    def test_addnewEvent(self, setup):
        # self.logger.info("******* Starting Test_001_DDT_Add event test **********")
        # self.logger.info("******* Starting Login DDT Test **********")
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

            self.subjpage.enterSubjectName(self.Subjectname)
            # self.ep.switchTopFrame() for Subjectdescription
            self.subjpage.getTopFrame()
            self.subjpage.getMceEdit(self.Subjectdescription)
            self.subjpage.switchToDefault()

            self.subjpage.enterAttend(self.Attend)
            self.subjpage.enterTags(self.Addtags)
            self.subjpage.enterIndividualPrice(self.Individualprice)
            self.subjpage.enterGroupPrice(self.Groupprice)
            self.subjpage.selectFile()
            # self.ep.switchTopFrame() for Subjecthighlights
            self.subjpage.getTopFrame1()
            self.subjpage.getMceEdit1(self.Subjecthighlights)
            self.subjpage.switchToDefault1()
            time.sleep(10)

            self.subjpage.saveButton()
            self.subjpage.previewButton()
            self.subjpage.submitSubject()

            act_title = self.driver.title
            Expected_title = "Tutors page | @iLRNU"

            if act_title == Expected_title:
                if self.exp == "Pass":
                    self.lp.tutor_logout();

# more than 5 subjects validation
# draft subject by clicking back  button
# Edit Subject
# delete subject
