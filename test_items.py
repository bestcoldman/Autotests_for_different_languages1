from selenium.webdriver.common.by import By
import time

class TestItemsCase1:
    def test_345(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
        assert button.is_enabled(), 'Purchase button is not active or doesnt exist.'
        time.sleep(10)