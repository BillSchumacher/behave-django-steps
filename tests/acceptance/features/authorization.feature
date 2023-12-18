# Created by billschumacher at 12/1/23
Feature: Authorization
  Test steps for authorization

  Scenario: User has a group or role assigned
    Given I am a registered user
    And I am assigned to the role "Admin"
    Then I should have the role "Admin"

  Scenario: User has no group or role assigned
    Given I am a registered user
    Then I should not have the role "Admin"

  Scenario: Custom admin page permission
    Given I am a registered user
    And I am assigned to the role "Admin"
    And the permission "Can View Admin Dashboard" with codename "can_view_admin_dashboard" for model "User" exists
    And the group "Admin" has the permission "Can View Admin Dashboard" with codename "can_view_admin_dashboard" for model "User"
    Then I should have the permission "can_view_admin_dashboard" for model "User"

  Scenario: No custom admin page permission
    Given I am a registered user
    And the permission "Can View Admin Dashboard" with codename "can_view_admin_dashboard" for model "User" exists
    And the group "Admin" has the permission "Can View Admin Dashboard" with codename "can_view_admin_dashboard" for model "User"
    Then I should not have the permission "can_view_admin_dashboard" for model "User"

  Scenario: Role that inherits from another role has permissions
    Given I am a registered user
    And the permission "Can View Admin Dashboard" with codename "can_view_admin_dashboard" for model "User" exists
    And the group "Admin" has the permission "Can View Admin Dashboard" with codename "can_view_admin_dashboard" for model "User"
    And I am assigned to the role "Admin User"
    And the role "Admin User" inherits permissions from the "Admin" role
    Then I should have the permission "can_view_admin_dashboard" for model "User"
    And the role "Admin User" should have the permissions from the "Admin" role
