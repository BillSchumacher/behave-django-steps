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
