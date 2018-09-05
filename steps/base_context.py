from pye2e import step
from data import page_url


@step('user is on "{page_name}" page')
def check_url(driver, page_name):
    driver.check_url(page_url.url[page_name])


@step('user goes to "{page_name}" page')
def open_page(driver, page_name):
    driver.open_url(page_url.url[page_name], add_base_url=False)

