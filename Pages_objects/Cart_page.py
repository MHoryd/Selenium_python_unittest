from Utilities.Support import Support

class Cart_page():


    def __init__(self,driver_object):
        self.driver = driver_object
        self.support = Support(self.driver)
        self.locators = {
            "total_price_xpath":"//tr[@class='cart-subtotal']//bdi",
            "remove_cap_from_cart_buttom_xpath":"//a[@href='https://tapsshop.pl/?product=cap']/ancestor::tr//a[@class='remove']",
            "remove_belt_from_cart_buttom_xpath":"//a[@href='https://tapsshop.pl/?product=belt']/ancestor::tr//a[@class='remove']",
            "remove_beanie_from_cart_buttom_xpath":"//a[@href='https://tapsshop.pl/?product=beanie']/ancestor::tr//a[@class='remove']",
            "belt_product_page_link_xpath":"//td[@class='product-name']/a[@href='https://tapsshop.pl/?product=belt']",
            "cap_product_page_link_xpath":"//td[@class='product-name']/a[@href='https://tapsshop.pl/?product=cap']",
            "beanie_product_page_link_xpath":"//td[@class='product-name']/a[@href='https://tapsshop.pl/?product=beanie']",
            "beanie_quantity_input_by_xpath":"//td[@class='product-name']/a[@href='https://tapsshop.pl/?product=beanie']/ancestor::tr//input",
            "update_cart_button_xpath":"//button[@name='update_cart']",
            "cart_was_updated_allert_xpath":"//div[contains(text(),'Koszyk zaktualizowany')]",
            "cart_is_empty_message_xpath":"//div[contains(text(),'Twój koszyk aktualnie jest pusty.')]"
        }


    def get_total_price(self):
        locator = self.locators['total_price_xpath']
        elem = self.support.get_elem(locator)
        return elem.text

    
    def click_remove_cap_buttom(self):
        locator = self.locators['remove_cap_from_cart_buttom_xpath']
        self.support.click_button_found_by_xpath(locator)


    def click_remove_belt_buttom(self):
        locator = self.locators['remove_belt_from_cart_buttom_xpath']
        self.support.click_button_found_by_xpath(locator)


    def click_remove_beanie_buttom(self):
        locator = self.locators['remove_beanie_from_cart_buttom_xpath']
        self.support.click_button_found_by_xpath(locator)


    def wait_untill_cap_will_be_removed(self):
        locator = self.locators['cap_product_page_link_xpath']
        self.support.wait_for_invisibility_of_elem_by_XPATH(locator)


    def wait_untill_belt_will_be_removed(self):
        locator = self.locators['belt_product_page_link_xpath']
        self.support.wait_for_invisibility_of_elem_by_XPATH(locator)


    def wait_untill_beanie_will_be_removed(self):
        locator = self.locators['beanie_product_page_link_xpath']
        self.support.wait_for_invisibility_of_elem_by_XPATH(locator)


    def clear_beanie_quantity_input(self):
        locator = self.locators['beanie_quantity_input_by_xpath']
        self.support.clear_text_in_input_by_xpath(locator)


    def insert_new_beanie_quantity(self,num):
        locator = self.locators['beanie_quantity_input_by_xpath']
        self.support.insert_text_into_input_found_by_xpath(locator, num)


    def update_cart(self):
        locator = self.locators['update_cart_button_xpath']
        self.support.click_button_found_by_xpath(locator)


    def wait_untill_cart_is_updated(self):
        locator = self.locators['cart_was_updated_allert_xpath']
        self.support.wait_for_visibility_of_elem_by_XPATH(locator)


    def assess_is_cart_empty(self):
        locator = self.locators['cart_is_empty_message_xpath']
        return self.support.elem_is_displayed_found_by_xpath(locator)
    
    
    def clear_all_items_in_cart_in_cart_page(self):
        elems = self.support.get_all_elems_in_cart_page()
        for elem in elems:
            elem.click()
        self.assess_is_cart_empty()