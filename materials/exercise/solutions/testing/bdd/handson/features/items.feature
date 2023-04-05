Feature: Items
Scenario: Add item to empty pocket
Given the hero has 0 items
When the hero picks up a  new item
Then he has 1 items


Scenario: Add item to fill pocket
Given the hero has 5 items
When the hero picks up a  new item
Then he has 5 items