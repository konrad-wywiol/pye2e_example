from pye2e import step
from data import page_url

search_input_xp = '//input[@id="lst-ib"]'
search_result_xp = '//div[@id="search"]//div[@class="g"]//cite[text()="%s"]'


@step('user searches for "{search_word}"')
def search_by_one(driver, search_word):
    driver.fill_element(search_input_xp, search_word, enter=True)


@step('user searches for "{search_word}" and "{search_word2}"')
def search_by_two(driver, search_word1, search_word2):
    driver.fill_element(search_input_xp, search_word1, clear=True)
    driver.fill_element(search_input_xp, ' ')
    driver.fill_element(search_input_xp, search_word2, enter=True)


@step('site "{site}" should be in results')
def confirm_search_results(driver, site):
    driver.element_is_visible(search_result_xp % page_url.url[site])




