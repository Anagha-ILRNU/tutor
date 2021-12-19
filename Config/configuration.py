from selenium.webdriver.chrome.options import Options
import pandas as pd


class TestData:
    # options = Options()
    # options.binary_location = "C://Program Files//Google//Chrome//Application//chrome.exe"
    CHROME_EXECUTABLE_PATH = "C:/Users/yoges/PycharmProjects/ilrnu/Config/Webdrivers/chromedriver.exe"
    FIREFOX_EXECUTABLE_PATH = "P:/Student_iLRNU/Config/Web Browser/geckodriver.exe"
    EDGE_EXECUTABLE_PATH = "P:/Student_iLRNU/Config/Web Browser/msedgedriver.exe"

    MAIN_URL = "https://uat.ilrnu.com"
    LOGIN_URL = "https://uat.ilrnu.com/login"
    DASHBOARD_URL = "https://uat.ilrnu.com/dashboard"
    SUBJECT_URL = "https://uat.ilrnu.com/tutor/subject/add/page1"

    LOGIN_PAGE_TITLE = "Login page | @iLRNU"
    DASHBOARD_TITLE = "My Dashboard | @iLRNU"
    TUTORPAGE_TITLE = "Tutors page | @iLRNU"

    EMAIL = "yatutor200@gmail.com"
    PASSWORD = "India@2020"

    # Testdata Tutor from Excel
    xlsx = pd.ExcelFile("P:/iLRNU application/Testdata/Logintutor.xlsx")
    df = pd.read_excel(xlsx, "Logintutor")
    Tutor = df

    # Testdata Student from Excel
    xlsx = pd.ExcelFile("P:/iLRNU application/Testdata/Loginstudent.xlsx")
    df1 = pd.read_excel(xlsx, "Loginstudent")
    Student = df1
