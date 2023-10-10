from behave import *

from tests.pages.base_page import BasePage
from tests.pages.contact_us_page import ContactUsPage
from tests.pages.login_portal_page import LoginPortalPage

use_step_matcher('re')

@When('I enter "(.*)" in the "(.*)" contact page input field')
def step_impl(context, content, field_name):
    page = ContactUsPage(context.driver)
    matching_fields = [input_field for input_field in page.feedbackInputs if
                             input_field.get_attribute("placeholder") == field_name]

    if len(matching_fields) > 0:
        matching_fields[0].send_keys(content)
    else:
        raise RuntimeError()

@When('I enter "(.*)" in the "(.*)" login portal input field')
def step_impl(context, content, field_name):
    page = LoginPortalPage(context.driver)
    matching_fields = [input_field for input_field in page.inputFields if
                             input_field.get_attribute("placeholder") == field_name]

    if len(matching_fields) > 0:
        matching_fields[0].send_keys(content)
    else:
        raise RuntimeError('Any element matches with the field_name')

@When('I click on the "(.*)" contact button')
def step_impl(context, button_name):
    page = ContactUsPage(context.driver)
    matching_buttons = [button for button in page.contactButtons if
                        button.get_attribute("value") == button_name]

    if len(matching_buttons) > 0:
        matching_buttons[0].click()
    else:
        raise RuntimeError('Any element matches with the expected button name ' + button_name)

@When('I click on the login portal link')
def step_impl(context):
    page = BasePage(context.driver)
    context.driver.execute_script("arguments[0].target='_self';", page.loginPortalLink)
    page.loginPortalLink.click()

@When('I click on the login button')
def step_impl(context):
    page = LoginPortalPage(context.driver)
    page.loginButton.click()
