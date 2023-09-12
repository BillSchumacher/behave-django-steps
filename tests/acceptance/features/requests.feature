# Created by billschumacher at 9/11/2023
Feature: Support requests

  Scenario: Create a simple model via DRF
    Given a "SimpleModel" model is available
    And the request has "name" with "test"
    When I make an API "POST" request to "/drf/simple/" with data
    Then status code "201" is returned
    And values exist in the response
    | name |
    | test |

  Scenario: Create a simple model via DRF Dynamic Rest
    Given a "SimpleModel" model is available
    And the request has "name" with "test"
    When I make an API "POST" request to "/dynamic/simple/" with data
    Then status code "201" is returned
    And values exist in "simple_model" in the response
    | name |
    | test |