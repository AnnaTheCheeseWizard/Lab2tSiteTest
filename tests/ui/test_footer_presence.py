from pages.home_page import HomePage

def test_tc_003_footer_presence(driver, wait):
    page = HomePage(driver, wait)
    page.open()
    
    assert page.is_footer_displayed(), "Нижня панель сайту не відображається"