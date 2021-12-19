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
