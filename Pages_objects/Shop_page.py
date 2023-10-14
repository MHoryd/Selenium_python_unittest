from Utilities.Support import Support

class Shop_page():


    def __init__(self,driver_object):
        self.driver = driver_object
        self.support = Support(self.driver)
        self.locators = {
            "add_beanie_to_cart_xpath":"//main//a[@data-product_sku='woo-beanie']",
            "add_belt_to_cart_xpath":"//main//a[@data-product_sku='woo-belt']",
            "add_cap_to_cart_xpath":"//main//a[@data-product_sku='woo-cap']",
            "adding_to_cart_in_progress_xpath":"//a[@class='button product_type_simple add_to_cart_button ajax_add_to_cart loading']",
            "hoodie_wit_logo_product_page_link_xpath":"//h2[contains(text(),'Hoodie with Logo')]"
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


    def wait_for_products_to_be_loaded_to_cart_after_button_click(self):
        locator=self.locators['adding_to_cart_in_progress_xpath']
        self.support.wait_for_invisibility_of_elem_by_XPATH(locator)
    

    def click_hoodie_with_logo_page_link(self):
        locator = self.locators['hoodie_wit_logo_product_page_link_xpath']
        self.support.click_button_found_by_xpath(locator)