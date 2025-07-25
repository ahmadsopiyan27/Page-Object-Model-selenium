import pytest
from selenium import webdriver
from pages.login_page import Login
from pages.inventory_page import Inventory
from pages.cart_page import Cart

@pytest.fixture
def setup():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get('https://www.saucedemo.com/')
    yield driver
    driver.quit()

@pytest.mark.positive
def test_checkout_flow(setup):
    login = Login(setup)
    inventory = Inventory(setup)
    cart = Cart(setup)

    login.input_username('standard_user')
    login.input_password('secret_sauce')
    login.click_login_button()

    cart.add_item_to_cart1()
    cart.add_item_to_cart2()
    cart.add_item_to_cart3()
    cart.go_to_cart()
    cart.click_checkout()
    cart.fill_checkout_form('Ahmad', 'Sofiyan', '12345')
    cart.finish_order()

    assert cart.get_order_status() == 'Thank you for your order!'
