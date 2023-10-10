class My_account_page():

    def __init__(self, driver_object,support_object):
        self.driver = driver_object
        self.support = support_object
        self.locators = {
            'my_account_header_xpath':"//h1[@class='entry-title']",
            'register_account_email_input_id':"reg_email",
            'register_account_button_xpath':"//button[@name='register']",
            'log_in_email_input_id':"username",
            'log_in_password_input_id':"password",
            'log_in_button_xpath':"//button[@name='login']",
            'invalid_both_credentials_xpath':"//ul[@class='woocommerce-error']/li[1]",
            'cockpit_nav_link_xpath':"//nav[@class='woocommerce-MyAccount-navigation']/ul/li[1]/a",
            'orders_nav_link_xpath':"//nav[@class='woocommerce-MyAccount-navigation']/ul/li[2]/a",
            'files_nav_link_xpath':"//nav[@class='woocommerce-MyAccount-navigation']/ul/li[3]/a",
            'address_nav_link_xpath':"//nav[@class='woocommerce-MyAccount-navigation']/ul/li[4]/a",
            'account_details_nav_link_xpath':"//nav[@class='woocommerce-MyAccount-navigation']/ul/li[5]/a",
            'log_out_nav_link_xpath':"//nav[@class='woocommerce-MyAccount-navigation']/ul/li[6]/a"
        }


    def insert_text_into_registration_input(self,text):
        locator = self.locators['register_account_email_input_id']
        elem = self.support.wait_for_visibility_of_elem_by_ID(locator)
        elem.send_keys(text)

    
    def click_registration_button(self):
        locator = self.locators['register_account_button_xpath']
        self.support.click_button_found_by_xpath(locator)


    def log_in_is_successful(self):
        locator = self.locators['my_account_header_xpath']
        return self.support.elem_is_displayed_found_by_xpath(locator)
    

    def insert_text_into_log_in_email_input(self,text):
        locator = self.locators['log_in_email_input_id']
        elem = self.support.wait_for_visibility_of_elem_by_ID(locator)
        elem.send_keys(text)
        

    def insert_text_into_log_in_password_input(self,text):
        locator = self.locators['log_in_password_input_id']
        elem = self.support.wait_for_visibility_of_elem_by_ID(locator)
        elem.send_keys(text)


    def click_log_in_button(self):
        locator = self.locators['log_in_button_xpath']
        self.support.click_button_found_by_xpath(locator)


    def get_invalid_both_credentials_error(self):
        locator = self.locators['invalid_both_credentials_xpath']
        elem = self.support.get_elem(locator)
        return elem.text
    

    def click_log_out_button(self):
        locator = self.locators['log_out_nav_link_xpath']
        self.support.click_button_found_by_xpath(locator)


    def log_out_is_successful(self):
        locator = self.locators['cockpit_nav_link_xpath']
        return self.support.wait_for_invisibility_of_elem_by_XPATH(locator)
        