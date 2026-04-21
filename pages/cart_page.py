from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):
    EMPTY_CART_MSG = (By.CLASS_NAME, "cart-empty")

    def open(self):
        self.driver.get("https://roll-club.ua/uk/cart/")

    def get_empty_message(self):
        return self.wait.until(self.ec.presence_of_element_located(self.EMPTY_CART_MSG))