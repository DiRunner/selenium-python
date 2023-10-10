from selenium.webdriver.common.by import By

from tests.locators.base_page import BasePageLocators


class LoginPortalPageLocators(BasePageLocators):
    INPUT_FIELDS = By.CSS_SELECTOR, '.form input'
    LOGIN_BUTTON = By.ID, 'login-button'
