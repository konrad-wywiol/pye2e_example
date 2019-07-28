Feature: As a user I want to be able to search by text

    Scenario Outline: Search by one word
        Given user is on "homepage" page
        When user searches for "<word>"
        Then site "<site>" should be in results

       Examples:
        | word     | site         |
        | python   | python.org   |
        | selenium | selenium.com |
    @wip
    Scenario: Search be two words
        Given user is on "homepage" page
        When user searches for "gherkin" and "cucumber"
        Then site "cucumber.io" should be in results
