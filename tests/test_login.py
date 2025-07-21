from selenium import webdriver
import pytest
from pages.login_page import login
from pages.inventory_page import Inventory


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
def test_login_positif(setup):
    login_page = login(setup)
    Inventory_page = Inventory(setup)

    login_page.input_username()
    login_page.input_password()
    login_page.click_login_button()
    title = Inventory_page.check_title()
    assert title == 'Swag Labs'
    '''
   
    '''

