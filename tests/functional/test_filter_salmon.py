from pages.home_page import HomePage

def test_tc_002_filter_salmon(driver, wait):
    page = HomePage(driver, wait)
    page.open()
    page.go_to_roles()
    page.filter_by_ingredient("Лосось")
    assert page.get_products_count() > 0