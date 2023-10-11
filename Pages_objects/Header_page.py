from Utilities.Support import Support

class Header_page():

    def __init__(self, driver_object):
        self.driver = driver_object
        self.support = Support(self.driver)
        self.locators = {
            "main_logo_xpath":"//a/img[@class='custom-logo']",
            "main_page_link_xpath":"//li[@id='menu-item-98']/a",
            "cart_page_link_xpath":"//li[@id='menu-item-99']/a",
            "my_account_link_xpath":"//li[@id='menu-item-100']/a",
            "orders_link_xpath":"//li[@id='menu-item-101']/a",
            "shop_link_xpath":"//li[@id='menu-item-102']/a",
            "search_input_xpath":"//header//input[@type='search']"

        }
    


    def click_my_account_button(self):
        locator = self.locators['my_account_link_xpath']
        self.support.click_button_found_by_xpath(locator)


    def click_shop_button(self):
        locator = self.locators['shop_link_xpath']
        self.support.click_button_found_by_xpath(locator)
    

    def insert_text_into_search_bar(self, text):
        locator = self.locators['search_input_xpath']
        self.support.insert_text_into_input_found_by_xpath(locator,text)


    def submit_search_bar_input(self):
        locator = self.locators['search_input_xpath']
        self.support.press_enter_at_element_found_by_xpath(locator)
