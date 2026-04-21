from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

class HomePage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

        self.roles_link_clickable = EC.element_to_be_clickable((By.LINK_TEXT, "Роли"))
        self.filter_btn_clickable = EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Види')]"))
        self.footer_present = EC.presence_of_element_located((By.TAG_NAME, "footer"))
        self.promo_link_clickable = EC.element_to_be_clickable((By.LINK_TEXT, "Акції"))
        self.products_present = EC.presence_of_all_elements_located((By.CLASS_NAME, "product"))

    def open(self):
        self.driver.get("https://roll-club.ua/uk/")

    def go_to_roles(self):
        self.wait.until(self.roles_link_clickable).click()

    def go_to_promotions(self):
        self.wait.until(self.promo_link_clickable).click()

    def ingredient_clickable(self, name):
        return EC.element_to_be_clickable((By.XPATH, f"//*[contains(text(), '{name}')]"))

    def filter_by_ingredient(self, name):
        self.wait.until(self.filter_btn_clickable).click()
        time.sleep(1) 
        self.wait.until(self.ingredient_clickable(name)).click()
        time.sleep(2) 

    def get_products_count(self):
        products = self.wait.until(self.products_present)
        return len(products)

    def is_footer_displayed(self):
        return self.wait.until(self.footer_present).is_displayed()