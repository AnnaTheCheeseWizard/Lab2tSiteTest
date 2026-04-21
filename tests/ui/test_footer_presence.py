from pages.home_page import HomePage

def test_tc_003_footer_presence(driver, wait):
    """Тест 3: Перевірка наявності футера"""
    page = HomePage(driver, wait)
    page.open()
    
    assert page.is_footer_displayed(), "Нижня панель сайту не відображається"