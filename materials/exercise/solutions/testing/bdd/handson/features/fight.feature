Feature: Fighting

Scenario: The Hero fights the wolf
Given the hero as a sword with 3 dmg and a wolf with 10 HP
When he attacks the wolf 1 time
Then the wolf has 7 hp left

Scenario: The hero kills the wolf
Given the hero as a sword with 3 dmg and a wolf with 10 HP
When he attacks the wolf 3 time
Then the wolf has 0 hp left