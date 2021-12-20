import pandas as pd
import numpy as np
import XLUtils
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time



#add events
#Edit events
#delete events
#report events
#publish events
#join event

# Chrome Webdrivers
options = Options()
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
driver = webdriver.Chrome(executable_path ="P:\iLRNU application\Config\Web Browser\chromedriver.exe")
driver.implicitly_wait(10)

## page objects###
