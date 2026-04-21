from pages.home_page import HomePage

class TestUI:
    def test_tc_003_footer_presence(self, driver):
        """Тест 3: Перевірка завантаження структури сторінки (Footer check)"""
        home_page = HomePage(driver)
        home_page.open()
        footer = home_page.get_footer()
        assert footer.is_displayed(), "Нижня панель (футер) сайту не завантажилась"