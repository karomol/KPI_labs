import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(ChromeDriverManager().install())

def test():
    search_word = 'nokia'

    driver.implicitly_wait(15)

    driver.get('https://allo.ua/')

    driver.find_element(By.ID, "search-form__input").send_keys(search_word, Keys.ENTER)
    time.sleep(3)
    result = driver.find_element(By.CSS_SELECTOR, 'div.product-card__content').text

    assert result.lower().__contains__(search_word.lower()), 'Error, the search word does not match the result'

    driver.quit()

test()
