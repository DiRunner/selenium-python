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
    def contactButtons(self):
        return self.driver.find_elements(*BasePageLocators.CONTACT_BUTTON)

    @property
    def contactReply(self):
        return self.driver.find_element(*BasePageLocators.CONTACT_REPLY)

    @property
    def loginPortalLink(self):
        return self.driver.find_element(*BasePageLocators.LOGIN_PORTAL_LINK)

