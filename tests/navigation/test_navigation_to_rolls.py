from pages.home_page import HomePage

def test_tc_001_navigation_to_rolls(driver, wait):
    page = HomePage(driver, wait)
    page.open()
    page.go_to_roles()
    assert "rolly" in driver.current_url