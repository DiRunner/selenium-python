from selenium.webdriver.common.by import By


class BasePageLocators:
    TITLE = By.CLASS_NAME, 'section_header'
    FEEDBACK_INPUT = By.CLASS_NAME, 'feedback-input'
    CONTACT_BUTTON = By.CLASS_NAME, 'contact_button'