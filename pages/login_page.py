from selenium.webdriver.common.by import By
from locaters.login import Loclogin

class Login:
    def __init__(self,driver):
        self.driver = driver

    def input_username(self,username):
        self.driver.find_element(By.ID,Loclogin.username_input).send_keys(username)

    def input_password(self,password):
        self.driver.find_element(By.ID,Loclogin.password_input).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.ID,Loclogin.login_button).click()
        
    def check_notif(self):
        pass