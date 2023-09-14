from selenium.webdriver.common.by import By

from tests.locators.base_page import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return 'http://www.webdriveruniversity.com/'

    @property
    def title(self):
        return self.driver.find_element(*BasePageLocators.TITLE)

    @property
    def feedbackInputs(self):
        return self.driver.find_elements(*BasePageLocators.FEEDBACK_INPUT)

    @property
    def contactButtons(self):
        return self.driver.find_elements(*BasePageLocators.CONTACT_BUTTON)

