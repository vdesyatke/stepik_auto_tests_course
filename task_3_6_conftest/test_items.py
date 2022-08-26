from selenium.webdriver.common.by import By
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_guest_should_see_addtobasket_button(browser):
    browser.get(link)
    time.sleep(5)
    assert browser.find_element(By.CSS_SELECTOR, '#add_to_basket_form > button.btn')