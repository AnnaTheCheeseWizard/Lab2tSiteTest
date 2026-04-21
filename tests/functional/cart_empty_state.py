from pages.cart_page import CartPage

def test_tc_004_cart_empty_state(driver):
    """Тест 4: Перевірка порожнього кошика"""
    cart_page = CartPage(driver)
    cart_page.open()
    empty_msg = cart_page.get_empty_message()
    assert empty_msg.is_displayed(), "Повідомлення про порожній кошик не знайдено"