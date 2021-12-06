from selenium.webdriver.chrome.options import Options
import pandas as pd


class TestData:
    # options = Options()
    # options.binary_location = "C://Program Files//Google//Chrome//Application//chrome.exe"
    CHROME_EXECUTABLE_PATH = "C:/Users/yoges/PycharmProjects/ilrnu/Config/Webdrivers/chromedriver.exe"
    FIREFOX_EXECUTABLE_PATH = "P:/Student_iLRNU/Config/Web Browser/geckodriver.exe"
    EDGE_EXECUTABLE_PATH = "P:/Student_iLRNU/Config/Web Browser/msedgedriver.exe"

    MAIN_URL = "https://uat.ilrnu.com"
    BASE_URL = "https://uat.ilrnu.com/login"
    DASHBOARD = "https://uat.ilrnu.com/dashboard"

    LOGIN_PAGE_TITLE = "https://uat.ilrnu.com/login"
    DASHBOARD_TITLE = "My Dashboard | @iLRNU"

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
