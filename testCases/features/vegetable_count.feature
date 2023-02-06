@regression
Feature: Vegetable Count

  Scenario: Verify brocolli count
    Given I navigate to GreenKart Page
    When  I increase vegetable quantity count
    Then  I verify quantity is correct

 Scenario: Verify cauliflower count
    Given I navigate to GreenKart Page
    When  I increase vegetable quantity count
    Then  I verify quantity is correct