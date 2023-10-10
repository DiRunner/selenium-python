from tests.locators.login_portal_page import LoginPortalPageLocators
from tests.pages.base_page import BasePage


class LoginPortalPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
    @property
    def url(self):
        return super(LoginPortalPage, self).url + 'Login-Portal/index.html'

    @property
    def inputFields(self):
        return self.driver.find_elements(*LoginPortalPageLocators.INPUT_FIELDS)

    @property
    def loginButton(self):
        return self.driver.find_element(*LoginPortalPageLocators.LOGIN_BUTTON)