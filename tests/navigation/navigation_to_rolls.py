from pages.home_page import HomePage

def test_tc_001_navigation_to_rolls(driver):
    """Тест 1: Перевірка переходу в розділ Роли"""
    home_page = HomePage(driver)
    home_page.open()
    home_page.go_to_roles()
    assert "rolly" in driver.current_url or "tovar-category" in driver.current_url