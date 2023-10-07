from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

class Support:

    def __init__(self, driver):
        self.driver = driver


    def wait_for_visibility_of_elem_by_XPATH(self, xpath, time_to_wait=5):
        try:
            elem = WebDriverWait(driver=self.driver,timeout=time_to_wait).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            return elem
        except TimeoutException:
            return False
        
    
    def wait_for_invisibility_of_elem_by_XPATH(self, xpath,time_to_wait=5):
        try:
            elem = WebDriverWait(driver=self.driver, timeout=time_to_wait).until(EC.invisibility_of_element_located((By.XPATH,xpath)))
            return elem
        except TimeoutException:
            return False


    def wait_for_visibility_of_elem_by_ID(self,ID, time_to_wait=5):
        try:
            elem = WebDriverWait(driver=self.driver,timeout=time_to_wait).until(EC.visibility_of_element_located((By.ID, ID)))
            return elem
        except TimeoutException:
            return False
        

    def wait_for_invisibility_of_elem_by_ID(self, ID,time_to_wait=5):
        try:
            elem = WebDriverWait(driver=self.driver, timeout=time_to_wait).until(EC.invisibility_of_element_located((By.ID,ID)))
            return elem
        except TimeoutException:
            return False
        

    def press_enter_at_element_found_by_xpath(self, xpath,time_to_wait=5):
        elem = WebDriverWait(driver=self.driver,timeout=time_to_wait).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        elem.send_keys(Keys.ENTER)