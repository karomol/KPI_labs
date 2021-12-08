from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def test():
    search_word = 'nokia'

    driver = webdriver.Chrome()
    driver.implicitly_wait(15)

    driver.get('https://allo.ua/')

    driver.find_element_by_id("search-form__input").send_keys(search_word)
    driver.find_element_by_id("search-form__input").send_keys(Keys.ENTER)

    time.sleep(3)
    result = driver.find_element_by_css_selector('div.product-card__content').text

    assert result.lower().__contains__(search_word.lower()), 'Error, the search word does not match the result'

    driver.quit()

test()