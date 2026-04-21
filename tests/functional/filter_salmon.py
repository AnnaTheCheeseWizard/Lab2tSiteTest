from pages.home_page import HomePage

def test_tc_002_filter_salmon(driver):
    """Тест 2: Фільтрація за інгредієнтом (Лосось)"""
    home_page = HomePage(driver)
    home_page.open()
    home_page.go_to_roles()
    home_page.filter_salmon()
    products = home_page.get_products()
    assert len(products) > 0, "Товари не знайдено після фільтрації"