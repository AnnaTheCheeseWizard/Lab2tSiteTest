from pages.cart_page import CartPage

def test_tc_004_cart_empty_state(driver, wait):
    page = CartPage(driver, wait)
    page.open()
    assert page.is_empty_message_displayed()