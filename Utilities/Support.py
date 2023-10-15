from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import uuid, re

class Support:

    def __init__(self, driver):
        self.driver = driver


    def hover_over_elem_by_ID(self,ID):
        elem = self.wait_for_visibility_of_elem_by_ID(ID=ID)
        action = ActionChains(self.driver)
        action.move_to_element(elem).perform()


    def hover_over_elem_and_click_by_ID(self,ID):
        elem = self.wait_for_visibility_of_elem_by_ID(ID=ID)
        action = ActionChains(self.driver)
        action.move_to_element(elem).click(elem).click(elem).perform()     


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
        

    def wait_for_visibility_of_elem_by_link_text(self,text,time_to_wait=5):
        try:
            elem = WebDriverWait(driver=self.driver, timeout=time_to_wait).until(EC.visibility_of_element_located((By.LINK_TEXT,text)))
            return elem
        except TimeoutException:
            return False




    def select_option_in_dropdown_by_text_elem_found_by_xpath(self,xpath,text):
        drop_elem = self.wait_for_visibility_of_elem_by_XPATH(xpath=xpath)
        dropdown = Select(drop_elem)
        dropdown.select_by_visible_text(text=text)


    def select_option_in_dropdown_by_text_elem_found_by_ID(self,ID,text):
        drop_elem = self.wait_for_invisibility_of_elem_by_ID(ID=ID)
        dropdown = Select(drop_elem)
        dropdown.select_by_visible_text(text=text)


    def dismiss_initial_notice(self):
        elem = self.wait_for_visibility_of_elem_by_XPATH(xpath="//a[@href='#']")
        elem.click()

    def press_enter_at_element_found_by_xpath(self, xpath):
        elem = self.wait_for_visibility_of_elem_by_XPATH(xpath=xpath)
        elem.send_keys(Keys.ENTER)


    def click_button_found_by_xpath(self, xpath):
        elem = self.wait_for_visibility_of_elem_by_XPATH(xpath=xpath)
        elem.click()


    def click_button_found_by_ID(self, ID):
        elem = self.wait_for_visibility_of_elem_by_ID(ID=ID)
        elem.click()

    def insert_text_into_input_found_by_xpath(self, xpath, text):
        elem = self.wait_for_visibility_of_elem_by_XPATH(xpath=xpath)
        elem.send_keys(text)

    def insert_text_into_input_found_by_ID(self, ID, text):
        elem = self.wait_for_visibility_of_elem_by_ID(ID=ID)
        elem.send_keys(text)


    def clear_text_in_input_by_ID(self,ID):
        elem = self.wait_for_visibility_of_elem_by_ID(ID)
        elem.clear()


    def clear_text_in_input_by_xpath(self,xpath):
        elem = self.wait_for_visibility_of_elem_by_XPATH(xpath)
        elem.clear()  


    def clear_text_in_input_by_ID(self,ID):
        elem = self.wait_for_visibility_of_elem_by_ID(ID)
        elem.clear()  


    def elem_is_displayed_found_by_xpath(self, xpath):
        elem = self.wait_for_visibility_of_elem_by_XPATH(xpath=xpath)
        return elem.is_displayed()
    

    def elem_is_displayed_found_by_partial_link_text(self, link_text):
        elem = self.wait_for_visibility_of_elem_by_link_text(link_text=link_text)
        return elem.is_displayed()
    
    
    def get_elem(self, xpath):
        elem = self.wait_for_visibility_of_elem_by_XPATH(xpath=xpath)
        return elem
    

    def get_random_email(self):
        return f'{uuid.uuid4()}@test.test'
    

    def get_number_from_string(self, text):
        match = re.search(r'\d+', text)
        number = int(match.group())
        return number

    def get_all_elems_in_cart_page(self):
        elems = self.driver.find_elements(By.XPATH,("//a[@class='remove']"))
        return elems

    def get_all_elems_in_cart_widget(self):
        elems = self.driver.find_elements(By.XPATH,("//a[@class='remove remove_from_cart_button']"))
        return elems