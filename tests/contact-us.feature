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

  Scenario: The reset button clean the entered information
    Given I am on the contact us page
    When I enter "test name" in the "First Name" input field
    And I enter "test last name" in the "Last Name" input field
    And I enter "test@test.com" in the "Email Address" input field
    And I enter "test comments" in the "Comments" input field
    And I click on the "RESET" contact button
    Then The "First Name" input field is empty
    And The "Last Name" input field is empty
    And The "Email Address" input field is empty
    And The "Comments" input field is empty

  Scenario: Submit contact us page give you a correct confirmation message
    Given I am on the contact us page
    When I enter "test name" in the "First Name" input field
    And I enter "test last name" in the "Last Name" input field
    And I enter "test@test.com" in the "Email Address" input field
    And I enter "test comments" in the "Comments" input field
    And I click on the "SUBMIT" contact button
    Then There is a reply message with content "Thank You for your Message!"
