from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

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


def test_login_positif(setup):
    '''
    login menggunakan user name pass yang benar
    '''
    setup.find_element(By.ID,'user-name').send_keys('standard_user')
    setup.find_element(By.ID,'password').send_keys('secret_sauce')
    setup.find_element(By.ID,'login-button').click()

    title = setup.find_element(By.XPATH, '//*[@id="header_container"]/div[1]/div[2]/div').text
    assert title == 'Swag Labs'
    setup.close

    '''
   
    '''

input_output = [
    ('sentot','secret_sauce', True),
    ('standard_user','sentot', True),
    ('sentot','sentot', True),

]

@pytest.mark.parametrize('username, password, notif', input_output)

def test_login_negatif_1(setup, username, password, notif):
    '''
    login menggunakan user name salah
    user name | password |  result
    salah       bener       gk bisa login
    bener       salah       gk bisa login
    salah       salah       ggk bisa login
    '''
    setup.find_element(By.ID,'user-name').send_keys('username')
    setup.find_element(By.ID,'password').send_keys('password')
    setup.find_element(By.ID,'login-button').click()

    notification_error = setup.find_element(By.XPATH, '//h3[@data-test="error"]').is_displayed()
    assert notification_error == notif
    # notification_text = driver.find_element(By.XPATH, '//h3[@data-test="error"]').text
    # assert notification_text == 'Epic sadface: Username and password do not match any user in this service'
