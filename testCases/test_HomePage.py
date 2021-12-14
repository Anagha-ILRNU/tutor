def test_homePageTitle(self):
    self.driver = webdriver.Chrome
    self.driver.get(homeURL)
    act_title = self.driver.Title
    self.driver.close()
    if act_title == "iLRNU - Empowering Tutors and Learners!":
        assert True
    else:
        assert False