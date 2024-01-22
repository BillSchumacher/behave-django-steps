Feature: Query Performance Steps

  Scenario: Test steps that ensure query performance
    When I execute the step `Given the permission "Can View Admin Dashboard" with codename "can_view_admin_dashboard" for model "User" exists` it should make "3" queries
    And I time the step `Given I am a registered user`
    Then the step `Given I am a registered user` execution should only take "0.5" seconds
