from Utilities.Support import Support

class Shop_page():


    def __init__(self,driver_object):
        self.driver = driver_object
        self.support = Support(self.driver)
        self.locators = {
            "product_in_cart_count":"//a[@class='cart-contents']/span[@class='count']",
            "add_beanie_to_cart_xpath":"//main//a[@data-product_sku='woo-beanie']",
            "add_belt_to_cart_xpath":"//main//a[@data-product_sku='woo-belt']",
            "add_cap_to_cart_xpath":"//main//a[@data-product_sku='woo-cap']",
            "cart_widget_id":"site-header-cart",
            "total_price_in_cart_widget_xpath":"//p[@class='woocommerce-mini-cart__total total']/span/bdi",
            "adding_to_cart_in_progress_xpath":"//a[@class='button product_type_simple add_to_cart_button ajax_add_to_cart loading']",
            "link_to_cart_page_from_widget_xpath":"//div[@class='widget_shopping_cart_content']//a[@href='https://tapsshop.pl/?page_id=7']",
            "remove_cap_from_cart_in_widget_xpath":"//ul[@id='site-header-cart']//a[@href='https://tapsshop.pl/?product=cap']/ancestor::li/a[@class='remove remove_from_cart_button']",
            "remove_belt_from_cart_in_widget_xpath":"//ul[@id='site-header-cart']//a[@href='https://tapsshop.pl/?product=belt']/ancestor::li/a[@class='remove remove_from_cart_button']",
            "remove_beanie_from_cart_in_widget_xpath":"//ul[@id='site-header-cart']//a[@href='https://tapsshop.pl/?product=beanie']/ancestor::li/a[@class='remove remove_from_cart_button']",
            "cart_is_empty_message_xpath":"//p[contains(text(),'Brak produktów w koszyku.')]"
        }

    def click_add_beanie_to_cart(self):
        locator = self.locators['add_beanie_to_cart_xpath']
        self.support.click_button_found_by_xpath(locator)


    def click_add_belt_to_cart(self):
        locator = self.locators['add_belt_to_cart_xpath']
        self.support.click_button_found_by_xpath(locator)


    def click_add_cap_to_cart(self):
        locator = self.locators['add_cap_to_cart_xpath']
        self.support.click_button_found_by_xpath(locator)


    def hover_over_cart_widget(self):
        locator = self.locators['cart_widget_id']
        self.support.hover_over_elem_by_ID(locator)


    def get_product_in_cart_count(self):
        locator = self.locators['product_in_cart_count']
        elem = self.support.get_elem(locator).text
        return self.support.get_number_from_string(elem)


    def get_total_price_from_cart_widget(self):
        locator = self.locators['total_price_in_cart_widget_xpath']
        elem = self.support.get_elem(locator)
        return elem.text
    

    def wait_for_products_to_be_loaded_to_cart_after_button_click(self):
        locator=self.locators['adding_to_cart_in_progress_xpath']
        self.support.wait_for_invisibility_of_elem_by_XPATH(locator)


    def click_cart_page_button_from_widget(self):
        locator = self.locators['link_to_cart_page_from_widget_xpath']
        self.support.click_button_found_by_xpath(locator)


    def click_remove_belt_from_cart_in_widget(self):
        locator = self.locators['remove_belt_from_cart_in_widget_xpath']
        self.support.click_button_found_by_xpath(locator)


    def click_remove_beanie_from_cart_in_widget(self):
        locator = self.locators['remove_beanie_from_cart_in_widget_xpath']
        self.support.click_button_found_by_xpath(locator)


    def click_remove_cap_from_cart_in_widget(self):
        locator = self.locators['remove_cap_from_cart_in_widget_xpath']
        self.support.click_button_found_by_xpath(locator)


    def wait_for_cap_to_be_removed_from_widget(self):
        locator = self.locators['remove_cap_from_cart_in_widget_xpath']
        self.support.wait_for_invisibility_of_elem_by_XPATH(locator)


    def click_remove_belt_buttom(self):
        locator = self.locators['remove_belt_from_cart_buttom_xpath']
        self.support.click_button_found_by_xpath(locator)


    def click_remove_beaniet_buttom(self):
        locator = self.locators['remove_beanie_from_cart_buttom_xpath']
        self.support.click_button_found_by_xpath(locator)


    def assess_is_cart_empty(self):
        locator = self.locators['cart_is_empty_message_xpath']
        return self.support.elem_is_displayed_found_by_xpath(locator)