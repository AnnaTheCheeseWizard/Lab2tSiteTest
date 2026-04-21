from selenium.webdriver.common.by import By
from .base_page import BasePage
import time

class HomePage(BasePage):
    ROLES_LINK = (By.LINK_TEXT, "Роли")
    FILTER_TYPES_BTN = (By.XPATH, "//*[contains(text(), 'Види')]")
    SALMON_OPTION = (By.XPATH, "//*[contains(text(), 'Лосось')]")
    PRODUCT_CARDS = (By.CLASS_NAME, "product")
    FOOTER = (By.TAG_NAME, "footer")
    PROMO_LINK = (By.LINK_TEXT, "Акції")

    def open(self):
        self.driver.get("https://roll-club.ua/uk/")

    def go_to_roles(self):
        self.wait.until(self.ec.element_to_be_clickable(self.ROLES_LINK)).click()

    def filter_salmon(self):
        self.wait.until(self.ec.element_to_be_clickable(self.FILTER_TYPES_BTN)).click()
        time.sleep(1)
        self.wait.until(self.ec.element_to_be_clickable(self.SALMON_OPTION)).click()
        time.sleep(2)

    def get_products(self):
        return self.driver.find_elements(*self.PRODUCT_CARDS)

    def get_footer(self):
        return self.wait.until(self.ec.presence_of_element_located(self.FOOTER))

    def go_to_promotions(self):
        self.wait.until(self.ec.element_to_be_clickable(self.PROMO_LINK)).click()