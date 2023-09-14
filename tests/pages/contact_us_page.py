from tests.pages.base_page import BasePage
from tests.locators.contact_us_page import ContactUsPageLocators


class ContactUsPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return super(ContactUsPage, self).url + '/Contact-Us/contactus.html'

    @property
    def FistName(self):
        return self.driver.find_elements(*ContactUsPageLocators.FIRST_NAME)

    @property
    def LastName(self):
        return self.driver.find_element(*ContactUsPageLocators.LASTNAME)

    @property
    def EmailAdress(self):
        return self.driver.find_element(*ContactUsPageLocators.EMAIL_ADDRESS)

    @property
    def Comments(self):
        return self.driver.find_element(*ContactUsPageLocators.COMMENTS)

