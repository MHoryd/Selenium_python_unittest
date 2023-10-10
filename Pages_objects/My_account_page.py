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
            'log_out_nav_link_xpath':"//nav[@class='woocommerce-MyAccount-navigation']/ul/li[6]/a",
            'edit_billing_address_button_xpath':"//div[@class='woocommerce-MyAccount-content']/div[2]/div[1]/header/a",
            'billing_address_display_xpath':"//div[@class='woocommerce-MyAccount-content']/div[2]/div[1]/address",
            'billing_country_dropdow_xpath':"//select",
            'billing_street_input_id':"billing_address_1",
            'billing_postal_code_id':"billing_postcode",
            'billing_city_id':"billing_city",
            'billing_phone_id':"billing_phone",
            'save_billing_address_button_xpath':"//button[@name='save_address']"
        }


    def insert_text_into_registration_input(self,text):
        locator = self.locators['register_account_email_input_id']
        self.support.insert_text_into_input_found_by_ID(locator,text)

    
    def click_registration_button(self):
        locator = self.locators['register_account_button_xpath']
        self.support.click_button_found_by_xpath(locator)


    def insert_text_into_log_in_email_input(self,text):
        locator = self.locators['log_in_email_input_id']
        self.support.insert_text_into_input_found_by_ID(locator,text)
        

    def insert_text_into_log_in_password_input(self,text):
        locator = self.locators['log_in_password_input_id']
        self.support.insert_text_into_input_found_by_ID(locator,text)


    def click_log_in_button(self):
        locator = self.locators['log_in_button_xpath']
        self.support.click_button_found_by_xpath(locator)


    def get_invalid_both_credentials_error(self):
        locator = self.locators['invalid_both_credentials_xpath']
        elem = self.support.get_elem(locator)
        return elem.text
    

    def click_address_nav_button(self):
        locator = self.locators['address_nav_link_xpath']
        self.support.click_button_found_by_xpath(locator)


    def click_log_out_button(self):
        locator = self.locators['log_out_nav_link_xpath']
        self.support.click_button_found_by_xpath(locator)


    def click_edit_address_button(self):
        locator = self.locators['edit_billing_address_button_xpath']
        self.support.click_button_found_by_xpath(locator)


    def select_value_in_address_country_dropdown(self,country):
        locator = self.locators['billing_country_dropdow_xpath']
        self.support.select_option_in_dropdown_by_text_elem_found_by_xpath(locator,country)


    def clear_text_in_billing_street_input(self):
        locator = self.locators['billing_street_input_id']
        self.support.clear_text_in_input_by_ID(locator)


    def clear_text_in_billing_postal_code_input(self):
        locator = self.locators['billing_postal_code_id']
        self.support.clear_text_in_input_by_ID(locator)


    def clear_text_in_billing_city_input(self):
        locator = self.locators['billing_city_id']
        self.support.clear_text_in_input_by_ID(locator)


    def clear_text_in_billing_phone_input(self):
        locator = self.locators['billing_phone_id']
        self.support.clear_text_in_input_by_ID(locator)


    def insert_text_into_billing_street_input(self, text):
        locator = self.locators['billing_street_input_id']
        self.support.insert_text_into_input_found_by_ID(locator, text)


    def insert_text_into_billing_postal_code_input(self, text):
        locator = self.locators['billing_postal_code_id']
        self.support.insert_text_into_input_found_by_ID(locator, text)


    def insert_text_into_billing_city_input(self, text):
        locator = self.locators['billing_city_id']
        self.support.insert_text_into_input_found_by_ID(locator, text)


    def insert_text_into_billing_phone_input(self,text):
        locator = self.locators['billing_phone_id']
        self.support.insert_text_into_input_found_by_ID(locator, text)


    def click_save_billing_address_button(self):
        locator = self.locators['save_billing_address_button_xpath']
        self.support.click_button_found_by_xpath(locator)


    def check_is_new_billing_adress_valid(self):
        locator = self.locators['billing_address_display_xpath']
        elem = self.support.get_elem(locator)
        return elem.text


    def log_out_is_successful(self):
        locator = self.locators['cockpit_nav_link_xpath']
        return self.support.wait_for_invisibility_of_elem_by_XPATH(locator)
        

    def log_in_is_successful(self):
        locator = self.locators['my_account_header_xpath']
        return self.support.elem_is_displayed_found_by_xpath(locator)
    

