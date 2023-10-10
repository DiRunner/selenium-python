from selenium.webdriver.common.by import By

from tests.locators.base_page import BasePageLocators


class ContactUsPageLocators(BasePageLocators):
    CONTACT_BUTTON = By.CLASS_NAME, 'contact_button'
    FEEDBACK_INPUT = By.CLASS_NAME, 'feedback-input'