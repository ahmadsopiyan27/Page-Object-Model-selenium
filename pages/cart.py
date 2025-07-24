from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Cart:
    def __init__(self, driver):
        self.driver = driver

    def add_item_to_cart1(self):
        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    
    def add_item_to_cart2(self):
        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light').click()

    def add_item_to_cart3(self):
        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()

    # Tunggu sampai URL berubah ke halaman cart
        WebDriverWait(self.driver, 10).until(
        EC.url_contains('/cart.html')
    )

    # Tunggu tombol checkout bisa diklik
        WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'checkout'))
    )
        

    def click_checkout(self):
        self.driver.find_element(By.ID, 'checkout').click()

    def fill_checkout_form(self, first, last, postal):
        self.driver.find_element(By.ID, 'first-name').send_keys(first)
        self.driver.find_element(By.ID, 'last-name').send_keys(last)
        self.driver.find_element(By.ID, 'postal-code').send_keys(postal)
        self.driver.find_element(By.ID, 'continue').click()

    def finish_order(self):
        self.driver.find_element(By.ID, 'finish').click()

    def get_order_status(self):
        return self.driver.find_element(By.CLASS_NAME, 'complete-header').text
    
