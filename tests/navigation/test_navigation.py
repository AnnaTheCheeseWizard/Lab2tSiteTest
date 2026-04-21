from pages.home_page import HomePage

class TestNavigation:
    def test_tc_001_navigation_to_rolls(self, driver):
        """Тест 1: Перевірка переходу в розділ Роли"""
        home_page = HomePage(driver)
        home_page.open()
        home_page.go_to_roles()
        assert "rolly" in driver.current_url or "tovar-category" in driver.current_url

    def test_tc_005_promotions_page(self, driver):
        """Тест 5: Перевірка переходу на сторінку Акцій (регресійний тест)"""
        home_page = HomePage(driver)
        home_page.open()
        home_page.go_to_promotions()
        assert "aktsii" in driver.current_url or "akcii" in driver.current_url