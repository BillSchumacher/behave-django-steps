Feature: Query Performance Steps

  Scenario: Test steps that ensure query performance
    When I execute the step `Given I am a superuser` it should make "16" queries
    And I time the step `Given I am a registered user`
    Then the step `Given I am a registered user` execution should only take "0.2" seconds


  Scenario: Test steps that ensure query performance with steps that have parameters
    When I execute the step `Given a "User" model is available` it should make "0" queries
