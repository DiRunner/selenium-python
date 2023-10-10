from tests.pages.base_page import BasePage
from tests.locators.contact_us_page import ContactUsPageLocators


class ContactUsPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return super(ContactUsPage, self).url + '/Contact-Us/contactus.html'

    @property
    def feedbackInputs(self):
        return self.driver.find_elements(*ContactUsPageLocators.FEEDBACK_INPUT)

    @property
    def contactButtons(self):
        return self.driver.find_elements(*ContactUsPageLocators.CONTACT_BUTTON)

    @property
    def ContactReply(self):
        return self.driver.find_element(*ContactUsPageLocators.CONTACT_REPLY)

