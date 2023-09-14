# Created by dcorredor at 9/14/2023
Feature: Test that contact us page has the correct content
  and works properly
  # Enter feature description here

  Scenario: contact us page has the correct content
    Given I am on the contact us page
    Then There is a title shown on the page
    And The title tag has content "CONTACT US"
    And There is a input field called "First Name"
    And There is a input field called "Last Name"
    And There is a input field called "Email Address"
    And There is a input field called "Comments"
    And There is a button called "RESET"
    And There is a button called "SUBMIT"