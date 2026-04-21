from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://roll-club.ua/uk/")

    def go_to_roles(self):
        roles_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Роли")))
        roles_link.click()

    def filter_salmon(self):
        filter_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Види')]")))
        filter_btn.click()
        time.sleep(1)
        salmon = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Лосось')]")))
        salmon.click()
        time.sleep(2)

    def get_products(self):
        return self.driver.find_elements(By.CLASS_NAME, "product")

    def get_footer(self):
        return self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "footer")))

    def go_to_promotions(self):
        promo_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Акції")))
        promo_link.click()