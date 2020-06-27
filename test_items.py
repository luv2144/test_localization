link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket_button_is_dispayed(browser):
    browser.get(link)
    button = browser.find_element_by_css_selector("#add_to_basket_form button")
    assert button.is_displayed(), f"There is no {button.text} button on the page"