from behave import *
from selenium import webdriver

from tests.pages.base_page import BasePage
from tests.pages.contact_us_page import ContactUsPage
from tests.pages.login_portal_page import LoginPortalPage

use_step_matcher('re')

@given('I am on the contact us page')
def step_impl(context):
    context.driver = webdriver.Chrome('C:/Users/dcorredor/Desktop/chromedriver.exe')
    page = ContactUsPage(context.driver)
    context.driver.get(page.url)

@given('I am on the home page')
def step_impl(context):
    context.driver = webdriver.Chrome('C:/Users/dcorredor/Desktop/chromedriver.exe')
    page = BasePage(context.driver)
    context.driver.get(page.url)

@given('I am on the login portal page')
def step_impl(context):
    context.driver = webdriver.Chrome('C:/Users/dcorredor/Desktop/chromedriver.exe')
    page = LoginPortalPage(context.driver)
    context.driver.get(page.url)

@then('I am on the login portal page')
def step_impl(context):
    expected_url = LoginPortalPage(context.driver).url
    assert context.driver.current_url == expected_url