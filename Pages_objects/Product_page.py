from Utilities.Support import Support

class Product_page():


    def __init__(self, driver_object):
        self.driver = driver_object
        self.support = Support(self.driver)
        self.locators = {
            "product_title":"//h1[@class='product_title entry-title']",
            "quantity_input_xpath":"//input[@name='quantity']",
            "add_to_cart_button":"//button[@name='add-to-cart']",
            "cart_was_updated_allert_xpath":"//div[@class='woocommerce-message']"
        }


    def get_product_name(self):
        locator = self.locators['product_title']
        elem = self.support.get_elem(locator)
        return elem.text
    

    def clear_quantity_iput(self):
        locator = self.locators['quantity_input_xpath']
        self.support.clear_text_in_input_by_xpath(locator)


    def insert_text_into_quantity_iput(self, text):
        locator = self.locators['quantity_input_xpath']
        self.support.insert_text_into_input_found_by_xpath(locator, text)


    def click_add_to_cart_button(self):
        locator = self.locators['add_to_cart_button']
        self.support.click_button_found_by_xpath(locator)


    def wait_untill_cart_is_updated(self):
        locator = self.locators['cart_was_updated_allert_xpath']
        self.support.wait_for_visibility_of_elem_by_XPATH(locator)