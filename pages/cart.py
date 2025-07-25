from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


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
        try:
            print("[INFO] Menunggu ikon keranjang bisa diklik...")
            cart_icon = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'shopping_cart_link'))
            )

            print("[INFO] Scroll ke ikon keranjang...")
            self.driver.execute_script("arguments[0].scrollIntoView(true);", cart_icon)

            print("[INFO] Klik ikon keranjang...")
            cart_icon.click()

            print("[INFO] Tunggu sampai URL berubah ke /cart.html...")
            WebDriverWait(self.driver, 10).until(
                EC.url_contains('/cart.html')
            )

            print("[INFO] Tunggu tombol checkout muncul...")
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'checkout'))
            )

            print("[INFO] Berhasil masuk halaman cart.")
        except TimeoutException as e:
            print("[ERROR] Gagal masuk halaman cart!")
            print("Current URL:", self.driver.current_url)
            raise e

        

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
    
