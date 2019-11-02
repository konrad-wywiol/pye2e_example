Feature: As a user I want to be able to search by image
    @disabled
    Scenario: Search by image
        Given user is on "homepage" page
        When user uploads "cat.jpg"
        Then site "cat_site" should be in results
