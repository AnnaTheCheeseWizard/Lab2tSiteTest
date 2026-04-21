from pages.home_page import HomePage
from pages.cart_page import CartPage

class TestFunctional:
    def test_tc_002_filter_salmon(self, driver):
        """Тест 2: Фільтрація за інгредієнтом (Лосось)"""
        home_page = HomePage(driver)
        # Оскільки фільтр працює на сторінці ролів, спочатку переходимо туди
        home_page.open()
        home_page.go_to_roles() 
        home_page.filter_salmon()
        products = home_page.get_products()
        assert len(products) > 0, "Товари не знайдено після фільтрації"

    def test_tc_004_cart_empty_state(self, driver):
        """Тест 4: Перевірка порожнього кошика"""
        cart_page = CartPage(driver)
        cart_page.open()
        empty_msg = cart_page.get_empty_message()
        assert empty_msg.is_displayed(), "Повідомлення про порожній кошик не відображається"