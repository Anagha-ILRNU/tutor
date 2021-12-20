import pandas as pd
import numpy as np
import XLUtils
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

# Chrome Webdrivers
options = Options()
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
driver = webdriver.Chrome(executable_path="P:\iLRNU application\Config\Web Browser\chromedriver.exe")
driver.implicitly_wait(10)

# Login Testdata
xlsx = pd.ExcelFile("P:\iLRNU application\Testdata\Create session.xlsx")
df = pd.read_excel(xlsx, "Logintutor")
print(df)
df1 = pd.read_excel(xlsx, "Create session")
print(df1)

# Click on Login
for i in range(len(df)):
    driver.get("http://uat.ilrnu.com")
    print(driver.current_url)
    driver.maximize_window()
    userprofilefield = driver.find_element(By.XPATH, "//*[name()='svg' and @data-icon='user-circle']").click()
    loginfield = driver.find_element(By.XPATH, "//p[text()='Log in']").click()
    print(driver.current_url)
    email = (df.loc[i, "Email"])
    password = (df.loc[i, "Password"])
    inputemail = driver.find_element(By.XPATH, "//input[@placeholder='Your mail id']").send_keys(email)
    inputpassword = driver.find_element(By.XPATH, "//input[@placeholder='Enter password']").send_keys(password)
    submitlogin = driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)
    # Get title of the page after clicking Login
    # result=[]
    for i in range(len(df1)):
        sessiontitle = (df1.loc[i, "Session title"])
        sessiondescription = (df1.loc[i, "Session description"])
        Default1 = (df1.loc[i, "Session type"])
        InPersonTutor = (df1.loc[i, "Session type"])
        liveTutoring = (df1.loc[i, "Session type"])
        sessionaddress = (df1.loc[i, "Session Address"])
        session = (df1.loc[i, "Session"])
        sessionsdate = (df1.loc[i, "Session sdate"])
        sessionedate = (df1.loc[i, "Session edate"])
        sessionstimehour = (df1.loc[i, "Session stime hour"])
        sessionstimemin = (df1.loc[i, "Session stime min"])
        sessionetimehour = (df1.loc[i, "Session etime hour"])
        sessionetimemin = (df1.loc[i, "Session etime min"])
        AMPM = (df1.loc[i, "AM/PM"])
        sessionduration = (df1.loc[i, "Session duration"])
        addstudent1 = (df1.loc[i, "Add Student1"])
        addstudent2 = (df1.loc[i, "Add Student2"])

        # Session information
        if driver.title == "My Dashboard | @iLRNU":
            # tutortab=driver.find_element(By.ID,'tutor-top-nav').click()
            # Write condition only if 1 subject added(create Session can be created)
            # createsession=driver.find_element(By.XPATH,"//span[text()='Create Session']").click()

            createsession = driver.find_element(By.XPATH,
                                                "(//div[contains(@class,'px-4 py-2 mx-auto text-center text-white rounded-md cursor-pointer lg:mx-0 text-md lg:min-w-32 lg:w-auto')][normalize-space()='Create Open Session'])[1]").click()

            # time.sleep(3)
            sessiontitle = driver.find_element(By.XPATH, "//input[@placeholder='Session Name']").send_keys(sessiontitle)

            #  Sessiondescription #
            # Find Top Frame
            top_frame = driver.find_element(By.XPATH, "//iframe[@class='tox-edit-area__iframe']")
            # Switch to top Frame
            driver.switch_to.frame(top_frame)
            # edit tinymce frame
            mce_edit = driver.find_element(By.XPATH, "//body[@class='mce-content-body ']")
            # Switch to mce_frame
            mce_edit.clear()
            mce_edit.send_keys(sessiondescription)
            # Back to Partent frame
            driver.switch_to.default_content()

            sessiontype = ["Default1", "InPersonTutor", "LiveTutoring"]

            # if sessiontype == Default1:
            #     Default1=driver.find_element(By.XPATH,"(//label[normalize-space()='Live Tutoring'])[1]").is_selected()
            #     session=driver.find_element(By.XPATH,"//label[normalize-space()='One Day session.']").is_selected()
            #     break

            # elif sessiontype == InPersonTutor:
            #     InPersonTutor=driver.find_element(By.XPATH,"(//label[normalize-space()='In-Person Tutoring'])[1]").is_selected()
            #     sessionAddress=driver.find_element(By.XPATH,"(//div[@class='flex flex-col items-center justify-center m-2 border rounded-lg cursor-pointer w-60 h-44'])[1]").send_keys(sessionaddress)

            # else:
            #     livetutoring=driver.find_element(By.XPATH,"(//label[normalize-space()='Live Tutoring'])[1]").is_selected()

            time.sleep(10)

            datetime = driver.find_element(By.XPATH, "//input[@placeholder='Select date and time']").click()
            # month=driver.find_element(By.XPATH,"(//option[@value='11'])[1]").click()
            # sdate=driver.find_element(By.XPATH,"//span[@aria-label='December 18, 2021']").send_keys(sessionsdate)
            # edate= #"//div[@class='dayContainer']/span[@aria-label='December 18, 2021']"

            starthour = driver.find_element(By.XPATH, "(//input[@aria-label='Hour'])[1]")

            starthour.send_keys(sessionstimehour)
            startmin = driver.find_element(By.XPATH, "(//input[@aria-label='Minute'])[1]")

            startmin.send_keys("30")
            time.sleep(2)
            AMPM = driver.find_element(By.XPATH,
                                       "(//span[@title='Click to toggle'][normalize-space()='AM'])[1]").click()
            # (//span[@title='Click to toggle'][normalize-space()='PM'])[1]")

            sessionduration = driver.find_element(By.XPATH, "//select[@id='dropdown']").send_keys(sessionduration)
            addstudent1 = driver.find_element(By.XPATH, "//input[@name='newStudent']").send_keys(addstudent1)
            addstu = driver.find_element(By.XPATH,
                                         "//button[@class='w-20 py-2 font-bold text-session_btn focus:outline-none']").click()
            addstudent2 = driver.find_element(By.XPATH, "//input[@name='newStudent']").send_keys(addstudent2)
            addstu1 = driver.find_element(By.XPATH,
                                          "//button[@class='w-20 py-2 font-bold text-session_btn focus:outline-none']").click()

            savesession = driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
            previewsession = driver.find_element(By.XPATH, "(//button[normalize-space()='Publish'])[1]").click()
            time.sleep(6)

            result = []
            if driver.title == "Tutors page | @iLRNU":
                print("Session added")
                result.append("Session added")
                verifysession = driver.find_element(By.XPATH, "//h3[text()='Upcoming']").click()
                home = driver.find_element(By.XPATH, "//div[contains(text(),'My Home')]").click()
                # checksession=driver.find_element(By.XPATH,"/(//h2[@class='text-base font-bold capitalize block w-full md:w-80 mb-1 md:mb-0'])[1]/")
                # checksession.is_displayed()

            else:
                print("Invalid Session")
                result.append("Invalid Session")

            df1.loc[i, "Result"] = result

            print(df1)
            df1.to_excel(xlsx, sheet_name="Create session", index=False)