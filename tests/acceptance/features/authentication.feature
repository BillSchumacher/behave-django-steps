# Created by billschumacher at 12/1/23
Feature: Authentication
  Test steps for authentication

  Scenario: Login as superuser
    Given I am a superuser
    Then I should be a superuser

  Scenario: Login as staff
    Given I am a staff user
    Then I should be a staff user

  Scenario: Login as user
    Given I am a registered user
    Then I should not be a superuser
    And I should not be a staff user

  Scenario: Inactive staff user with first and last name
    Given the user has a first name of "Bob"
    And the user has a last name of "Smith"
    And the user is not active
    And the user is staff
    And I am a registered user
    Then I should not be a superuser
    And I should be a staff user
    And I should not be an active user
    And I should have a first name of "Bob"
    And I should have a last name of "Smith"
