from behave import *
from selenium import webdriver

from tests.pages.contact_us_page import ContactUsPage

use_step_matcher('re')

@given('I am on the contact us page')
def step_impl(context):
    context.driver = webdriver.Chrome('C:/Users/dcorredor/Desktop/chromedriver.exe')
    page = ContactUsPage(context.driver)
    context.driver.get(page.url)