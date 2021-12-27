from selenium.webdriver.support import expected_conditions as EC


# Parent class for all pages
# It contains all the generic methods and utilities for all the pages


class BasePage:

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    def wait_until_element_is_clickable(self, locator_type, locator):
        element = self.wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return element

    def wait_for_presence_of_all_elements(self, locator_type, locator):
        list_of_elements = self.wait.until(EC.presence_of_all_elements_located((locator_type, locator)))
        return list_of_elements

    def is_signup_link_exist(self):
        return self.is_visible(self.SIGNUP_LINK)

    def wait_for_element_visibility(self, waitTime, locatorMode, Locator):
        element = None
        if locatorMode == LocatorMode.ID:
            element = WebDriverWait(self.driver, waitTime). \
                until(EC.visibility_of_element_located((By.ID, Locator)))
        elif locatorMode == LocatorMode.NAME:
            element = WebDriverWait(self.driver, waitTime). \
                until(EC.visibility_of_element_located((By.NAME, Locator)))
        elif locatorMode == LocatorMode.XPATH:
            element = WebDriverWait(self.driver, waitTime). \
                until(EC.visibility_of_element_located((By.XPATH, Locator)))
        elif locatorMode == LocatorMode.CSS_SELECTOR:
            element = WebDriverWait(self.driver, waitTime). \
                until(EC.visibility_of_element_located((By.CSS_SELECTOR, Locator)))
        else:
            raise Exception("Unsupported locator strategy.")
        return element

    def find_element(self, locatorMode, Locator):
        element = None
        if locatorMode == LocatorMode.ID:
            element = self.driver.find_element_by_id(Locator)
        elif locatorMode == LocatorMode.NAME:
            element = self.driver.find_element_by_name(Locator)
        elif locatorMode == LocatorMode.XPATH:
            element = self.driver.find_element_by_xpath(Locator)
        elif locatorMode == LocatorMode.CSS_SELECTOR:
            element = self.driver.find_element_by_css_selector(Locator)
        else:
            raise Exception("Unsupported locator strategy.")
        return element

    def fill_out_field(self, locatorMode, Locator, text):
        self.find_element(locatorMode, Locator).clear()
        self.find_element(locatorMode, Locator).send_keys(text)

    def click(self, waitTime, locatorMode, Locator):
        self.wait_until_element_clickable(waitTime, locatorMode, Locator).click()

    def hover_over(self, waitTime, locatorMode, Locator):
        element = Locator
        self.wait_for_element_visibility(waitTime, locatorMode, Locator).move_to_element(element).perform()

    # def do_click(self, by_locator):
    #     WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()
    #
    # def do_send_keys(self, by_locator, text):
    #     WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
    #
    # def get_element_text(self, by_locator):
    #     element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
    #     return element.text
    #
    # def is_visible(self, by_locator):
    #     element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
    #     return bool(element)
    #
    # def get_title(self, by_locator):
    #     WebDriverWait(self.driver, 10).until(EC.title_is(title))
    #     return self.driver.title
    #
    # def is_enabled(self, by_locator):
    #     element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
    #     return bool(element)
