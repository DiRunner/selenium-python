from selenium.webdriver.common.by import By


class BasePageLocators:
    TITLE = By.CLASS_NAME, 'section_header'
    LOGIN_PORTAL_LINK = By.ID, 'login-portal'
    CONTACT_REPLY = By.ID, 'contact_reply'
