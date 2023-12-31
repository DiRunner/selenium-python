from behave import *
from selenium import webdriver

from tests.pages.base_page import BasePage

use_step_matcher('re')


@then('There is a title shown on the page')
def step_impl(context):
    page = BasePage(context.driver)
    assert page.title.is_displayed()


@then('The title tag has content "(.*)"')
def step_impl(context, content):
    page = BasePage(context.driver)
    assert page.title.text == content


@then('There is a input field called "(.*)"')
def step_impl(context, name):
    page = BasePage(context.driver)
    input_field_with_name = [input_field for input_field in page.feedbackInputs if
                             input_field.get_attribute("placeholder") == name]

    assert len(input_field_with_name) > 0
    assert all([input_field.is_displayed() for input_field in input_field_with_name])


@then('There is a button called "(.*)"')
def step_impl(context, name):
    page = BasePage(context.driver)
    button_with_name = [button for button in page.contactButtons if
                        button.get_attribute("value") == name]

    assert len(button_with_name) > 0
    assert all([button.is_displayed() for button in button_with_name])

@then('The "(.*)" input field is empty')
def step_impl(context, field_name):
    page = BasePage(context.driver)
    matching_fields = [button for button in page.feedbackInputs if
                        button.get_attribute("placeholder") == field_name]

    assert len(matching_fields) > 0
    assert all([input_field.get_attribute("value") == '' for input_field in matching_fields])

@then('There is a reply message with content "(.*)"')
def step_impl(context, content):
    page = BasePage(context.driver)
    assert page.contactReply.is_displayed()
    assert page.contactReply.text == content

@then('An alert with "(.*)" message displays')
def step_impl(context, content):
    alert = context.driver.switch_to.alert
    assert content in alert.text
