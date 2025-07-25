from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locaters.cart import LocCart

class Cart:
    def __init__(self, driver):
        self.driver = driver

    def add_item_to_cart1(self):
        self.driver.find_element(By.ID, LocCart.add_cart_backpack).click()

    def add_item_to_cart2(self):
        self.driver.find_element(By.ID, LocCart.add_cart_bike_light).click()

    def add_item_to_cart3(self):
        self.driver.find_element(By.ID, LocCart.add_cart_tshirt).click()

    def go_to_cart(self):
        cart_icon = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, LocCart.cart_icon))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", cart_icon)
        cart_icon.click()

        WebDriverWait(self.driver, 10).until(
            EC.url_contains('/cart.html')
        )
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, LocCart.checkout_button))
        )

    def click_checkout(self):
        self.driver.find_element(By.ID, LocCart.checkout_button).click()

    def fill_checkout_form(self, first, last, postal):
        self.driver.find_element(By.ID, LocCart.first_name_input).send_keys(first)
        self.driver.find_element(By.ID, LocCart.last_name_input).send_keys(last)
        self.driver.find_element(By.ID, LocCart.postal_code_input).send_keys(postal)
        self.driver.find_element(By.ID, LocCart.continue_button).click()

    def finish_order(self):
        self.driver.find_element(By.ID, LocCart.finish_button).click()

    def get_order_status(self):
        return self.driver.find_element(By.CLASS_NAME, LocCart.order_status_text).text
