from data import page_url

class Homepage:
    search_input_xp = '//div[@id="searchform"]//input[@role="combobox"]'
    search_result_xp = '//div[@id="search"]//cite[contains(text(),"%s")]'

    def search_by_one(self, driver, search_word):
        driver.fill_element(self.search_input_xp, search_word, enter=True)

    def search_by_two(self, driver, search_word1, search_word2):
        driver.fill_element(self.search_input_xp, search_word1, clear=True)
        driver.fill_element(self.search_input_xp, ' ')
        driver.fill_element(self.search_input_xp, search_word2, enter=True)

    def confirm_search_results(self, driver, site):
        driver.element_is_visible(self.search_result_xp % page_url.url[site])


homepage = Homepage()
