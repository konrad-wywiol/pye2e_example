Feature: As a user I want to be able to search by image
    @disabled
    Scenario: Search by image
        Given user is on "homepage" page
        When user uploads "xsolve.logo"
        Then Then site "xsolve.software" should be in results
