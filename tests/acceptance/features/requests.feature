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
    And the request has "truthy" boolean false
    And the request has "numeric" with 42
    When I make an API "POST" request to "/dynamic/simple/" with data
    And the data for "test_app" is dumped
    Then status code "201" is returned
    And values exist in "simple_model" in the response
    | name | truthy | numeric |
    | test | False  | 42      |

  Scenario: Query a simple model via DRF Dynamic Rest loaded from fixture
    Given a "SimpleModel" model is available
    And these fixtures are used "test_app"
    And the request has "name" with "test"
    When I make an API "GET" request to "/dynamic/simple/" with data
    Then status code "200" is returned
    And values exist in "simple_models" in the response
    | name |
    | test |


  Scenario: Create a related model via DRF Dynamic Rest
    Given a "SimpleModel" model is available
    And the request has "name" with "test"
    And the request has "truthy" boolean false
    And the request has "numeric" with 42
    When I make an API "POST" request to "/dynamic/simple/" with data
    Then status code "201" is returned
    And values exist in "simple_model" in the response
    | name | truthy | numeric |
    | test | False  | 42      |
    When I make an API "GET" request to "/dynamic/simple/?filter{name}=test" with data
    Then status code "200" is returned
    And values exist in "simple_models" in the response
    | name | truthy | numeric |
    | test | False  | 42      |
    Given a "RelatedModel" model is available
    And the request data is reset
    And the request has "simple" with "3"
    When I make an API "POST" request to "/dynamic/related/" with data
    And the data for "test_app" is dumped
    Then status code "201" is returned
    And values exist in "related_model" in the response
    | owner |
    | None  |
    And values exist in "related_model" in the response
    | owner |
    |       |
