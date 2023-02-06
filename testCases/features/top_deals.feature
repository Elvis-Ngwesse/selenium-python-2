@regression
Feature: Top Deals
    Search for vegetables and select appropriate deals

  @deal
  Scenario: Search for tomato deal
      Given I navigate to GreenKart Page
      When  I click on top deals
      And   I navigate to offers page
      And   I search for vegetable "tomato"
      Then  I verify "Tomato", "37" and "26"

  @count
  Scenario: Search for wheat deal
      Given I navigate to GreenKart Page
      When  I click on top deals
      And   I navigate to offers page
      And   I search for vegetable "wheat"
      Then  I verify "Wheat", "67" and "28"

  @view
  Scenario: View offers
      Given I navigate to GreenKart Page
      When  I click on top deals
      And   I navigate to offers page and back
      Then  I verify page url