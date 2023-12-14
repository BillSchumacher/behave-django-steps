Feature: Query Performance Steps

  Scenario: Test steps that ensure query performance
    Given I have a queryset
    When I execute the step "I use the queryset" it should only make "2" queries
    Then the step should be executed in less than 1 second
