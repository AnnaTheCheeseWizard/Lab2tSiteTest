from pages.home_page import HomePage
from pages.cart_page import CartPage

class TestRollClubUI:
    def test_tc_001_navigation_to_rolls(self, driver):
        """Тест 1: Перевірка переходу в розділ Роли"""
        home_page = HomePage(driver)
        home_page.open()
        home_page.go_to_roles()
        assert "rolly" in driver.current_url or "tovar-category" in driver.current_url

    def test_tc_002_filter_salmon(self, driver):
        """Тест 2: Фільтрація за інгредієнтом (Лосось)"""
        home_page = HomePage(driver)
        home_page.filter_salmon()
        products = home_page.get_products()
        assert len(products) > 0, "Товари не знайдено після фільтрації"

    def test_tc_003_footer_presence(self, driver):
        """Тест 3: Перевірка завантаження структури сторінки (Footer check)"""
        home_page = HomePage(driver)
        home_page.open()
        footer = home_page.get_footer()
        assert footer.is_displayed(), "Нижня панель сайту не завантажилась"

    def test_tc_004_cart_empty_state(self, driver):
        """Тест 4: Перевірка порожнього кошика"""
        cart_page = CartPage(driver)
        cart_page.open()
        empty_msg = cart_page.get_empty_message()
        assert empty_msg.is_displayed()

    def test_tc_005_promotions_page(self, driver):
        """Тест 5: Перевірка переходу на сторінку Акцій (регресійний тест)"""
        home_page = HomePage(driver)
        home_page.open()
        home_page.go_to_promotions()
        assert "aktsii" in driver.current_url or "akcii" in driver.current_url