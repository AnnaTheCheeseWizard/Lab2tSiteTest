from pages.home_page import HomePage

def test_tc_005_promotions_page(driver):
    """Тест 5: Перевірка переходу на сторінку Акцій"""
    home_page = HomePage(driver)
    home_page.open()
    home_page.go_to_promotions()
    assert "aktsii" in driver.current_url or "akcii" in driver.current_url