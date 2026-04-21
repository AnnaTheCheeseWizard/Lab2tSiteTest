from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        
        self.empty_msg_visible = EC.visibility_of_element_located((By.CLASS_NAME, "cart-empty"))

    def open(self):
        self.driver.get("https://roll-club.ua/uk/cart/")

    def is_empty_message_displayed(self):
        return self.wait.until(self.empty_msg_visible).is_displayed()