from pages.home_page import HomePage

def test_tc_005_promotions_page(driver, wait):
    page = HomePage(driver, wait)
    page.open()
    page.go_to_promotions()
    assert "aktsii" in driver.current_url or "akcii" in driver.current_url