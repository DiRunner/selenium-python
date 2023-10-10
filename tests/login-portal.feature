# Created by dcorredor at 10/2/2023
Feature: Test that login portal has the correct content and works properly

  Scenario: Check that login button opens the login portal
    Given I am on the home page
    When I click on the login portal link
    Then I am on the login portal page

  Scenario: Check that invalid user can't login to the portal
    Given I am on the login portal page
    When I enter "testUser" in the "Username" login portal input field
    And I enter "testPassword" in the "Password" login portal input field
    And I click on the login button
    Then An alert with "validation faileds" message displays
