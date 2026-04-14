import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def driver():
    options = webdriver.EdgeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Edge(options=options)
    yield driver
    driver.quit()

class TestRollClubUI:
    def test_tc_001_navigation_to_rolls(self, driver):
        """Тест 1: Перевірка переходу в розділ Роли"""
        driver.get("https://roll-club.ua/uk/")
        wait = WebDriverWait(driver, 10)
        roles_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Роли")))
        roles_link.click()
        # Тут спеціально стара версія, яка впаде (roli замість rolly)
        assert "roli" in driver.current_url