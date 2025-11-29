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
    driver.get('http://172.16.151.112:3000') 
    yield driver
    driver.quit()   


def test_login_positif(setup):
    '''
    Validasi Login Scenario Valid Login succes
    '''
    setup.find_element(By.XPATH,'(//input[@placeholder='Email'])[1]').send_keys('test.qa@trimegah.com')
    setup.find_element(By.XPATH,'(//input[@placeholder='Password'])[1]').send_keys('Tr!m@12345')
    setup.find_element(By.XPATH,'(//button[normalize-space()='Login'])[1]').click()

    title = setup.find_element(By.XPATH, '(//h1[normalize-space()='Demo Shop'])[1]').text
    assert title == 'Demo Shop'
    setup.close

    # '''
   
    # '''

# input_output = [
#     ('sentot','secret_sauce', True),
#     ('standard_user','sentot', True),
#     ('sentot','sentot', True),

# ]

# @pytest.mark.parametrize('username, password, notif', input_output)

# def test_login_negatif_1(setup, username, password, notif):
#     '''
#     login menggunakan user name salah
#     user name | password |  result
#     salah       bener       gk bisa login
#     bener       salah       gk bisa login
#     salah       salah       ggk bisa login
#     '''
#     setup.find_element(By.ID,'user-name').send_keys('username')
#     setup.find_element(By.ID,'password').send_keys('password')
#     setup.find_element(By.ID,'login-button').click()

#     notification_error = setup.find_element(By.XPATH, '//h3[@data-test="error"]').is_displayed()
#     assert notification_error == notif
#     # notification_text = driver.find_element(By.XPATH, '//h3[@data-test="error"]').text
#     # assert notification_text == 'Epic sadface: Username and password do not match any user in this service'
