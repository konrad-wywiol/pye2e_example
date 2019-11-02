from pye2e import step
from data import page_url
from pages.homepage import homepage


@step('user searches for "{search_word}"')
def search_by_one(driver, search_word):
    homepage.search_by_one(driver, search_word)


@step('user searches for "{search_word}" and "{search_word2}"')
def search_by_two(driver, search_word1, search_word2):
    homepage.search_by_two(driver, search_word1, search_word2)


@step('site "{site}" should be in results')
def confirm_search_results(driver, site):
    homepage.confirm_search_results(driver, site)
