from selenium.webdriver.common.by import By
from locaters.inventory import LocInventory
from selenium.webdriver.common.action_chains import ActionChains

class Inventory :
    def __init__(self, driver):
        self.driver = driver


    def check_title(self):
        title = self.driver.find_element(By.XPATH,LocInventory.title_text ).text

        return title
    
    
    
