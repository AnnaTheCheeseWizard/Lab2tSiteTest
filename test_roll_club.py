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
        assert "rolly" in driver.current_url or "tovar-category" in driver.current_url

    def test_tc_002_filter_salmon(self, driver):
        """Тест 2: Фільтрація за інгредієнтом (Лосось)"""
        wait = WebDriverWait(driver, 10)
        filter_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Види')]")))
        filter_btn.click()
        time.sleep(1)
        salmon = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Лосось')]")))
        salmon.click()
        time.sleep(2)
        products = driver.find_elements(By.CLASS_NAME, "product")
        assert len(products) > 0, "Товари не знайдено після фільтрації"

    def test_tc_003_cart_empty_state(self, driver):
        """Тест 4: Перевірка порожнього кошика"""
        driver.get("https://roll-club.ua/uk/cart/")
        wait = WebDriverWait(driver, 10)
        empty_msg = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart-empty")))
        assert empty_msg.is_displayed()

    def test_tc_004_footer_presence(self, driver):
        """Тест 3: Перевірка завантаження структури сторінки (Footer check)"""
        driver.get("https://roll-club.ua/uk/")
        wait = WebDriverWait(driver, 10)
        footer = wait.until(EC.presence_of_element_located((By.TAG_NAME, "footer")))
        assert footer.is_displayed(), "Нижня панель сайту не завантажилась"