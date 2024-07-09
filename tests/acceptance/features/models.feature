# Created by billschumacher at 9/11/2023
Feature: Django models support
  Background: Models are added to the context for easy access.
    Given models are available

  Scenario: A known model is in the context.
    Then a "User" model is available

  Scenario: Create a known model
    Given a "User" model is available
    And a "User" with values
      | username | password  |
      | test     | test      |
    Then a "User" with values exists
      | username |
      | test     |
    And a "User" with values does not exist
      | username |
      | bob      |
  
  Scenario: Set a known model fields
    Given a "User" model is available
    And a "User" with values
      | username | password  |
      | test     | test      |
    And context "User" values set to
      | username |
      | evlampiy |
    Then a "User" with values exists
      | username |
      | evlampiy |
    And a "User" with values does not exist
      | username |
      | test     |
