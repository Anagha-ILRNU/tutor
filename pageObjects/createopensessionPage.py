import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class CreateSessionPage:
    # Session Locators
    btn_createSessionHome = "(//div[contains(@class,'px-4 py-2 mx-auto text-center text-white rounded-md cursor-pointer lg:mx-0 text-md lg:min-w-32 lg:w-auto')][normalize-space()='Create Open Session'])[1]"

    btn_createSessionTutoring = "(//span[@class='hidden pl-2 font-bold md:block'])[1]"

    drp_subjectName = "(//select[@name='subjectId'])[1]"

    txt_sessionTitle = "(//input[@placeholder='Session Name'])[1]"
    rdb_liveTutoring = "(//input[@id='liveTutoring'])[1]"
    rdb_inPersonTutoring = "(//input[@id='inPersonTutoring'])[1]"

    # Enter Address details for inpersontutoring
    btn_address = "(//div[@class='flex flex-col items-center justify-center m-2 border rounded-lg cursor-pointer w-60 h-44'])[1]"
    btn_change = "(//span[@class='text-red-400 cursor-pointer hover:text-red-500'])[1]"
    txt_searchArea = "(//input[@placeholder='Search for area, street name...'])[1]"
    sel_selectAddress = "(//div[normalize-space()='Yellappa Chetty Layout, Sivanchetti Gardens, Halasuru, Karnataka, India'])[1]"
    confirmLocation = "check bala"
    txt_addressTitle = "(//input[@id='addressTitle'])[1]"
    txt_houseFlat = "(//input[@id='flatNo'])[1]"
    txt_landmark = "(//input[@id='landmarkArea'])[1]"
    btn_save = "(//button[normalize-space()='save'])[1]"

    drp_sessionTimeZone = "(//select[@class='w-full px-2 py-2 mt-2 mr-2 bg-gray-200 rounded-md lg:w-108 focus:outline-none'])[1]"
    sel_sessiondate = "(//input[@id='new_date_component'])[1]"
    drp_month = "(//select[@aria-label='Month'])[1]"
    drp_year = "(//input[@aria-label='Year'])[1]"
    sel_selectDate = "(//div[@class='dayContainer'])[1]"
    drp_sessionduration = "(//select[@id='dropdown'])[1]"
    sel_sessionRecurrence = "(//option[normalize-space()='Does not repeat'])[1]"

    # select_customRecurrence
    sel_repeatEvery = "(//input[@value='1'])[1]"
    sel_repeatEveryWeek = "(//option[normalize-space()='week(s)'])[1]"
    sel_repeatEveryday = "(//option[normalize-space()='day(s)'])[1]"

    sel_sessionRecurrence1 = "(//option[@value='custom'])[1]"

    sel_repeatonSunday = "(//div[@class='text-sm'][normalize-space()='S'])[1]"
    sel_repeatonMonday = "(//div[@class='text-sm'][normalize-space()='M'])[1]"
    sel_repeatonTuesday = "(//div[@class='text-sm'][normalize-space()='T'])[1]"
    sel_repeatonWednesday = "(//div[contains(text(),'W')])[1]"
    sel_repeatonThursday = "(//div[@class='text-sm'][normalize-space()='T'])[2]"
    sel_repeatonFriday = "(//div[contains(text(),'F')])[1]"
    sel_repeatonSaturaday = "(//div[@class='text-sm'][normalize-space()='S'])[2]"

    sel_endOn = "(//input[@name='recur_mode'])[1]"
    sel_repeatEvery1 = "(//input[@value='2'])[1]"
    sel_repeatMonth = "(//select[@aria-label='Month'])[3]"
    sel_repeatyear = "(//div[@class='numInputWrapper'])[9]"
    sel_endafter = "(//input[@name='recur_mode'])[2]"
    sel_Ok = "(//div[@class='text-base font-medium cursor-pointer text-logo_blue'])[1]"

    txt_addStudent = "(//input[@name='newStudent'])[1]"
    btn_addStudent = "(//button[@class='w-20 py-2 font-bold text-session_btn focus:outline-none'])[1]"

    def __init__(self, driver):
        self.driver = driver


