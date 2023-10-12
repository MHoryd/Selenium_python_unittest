from Utilities.Support import Support

class Shop_page():


    def __init__(self,driver_object):
        self.driver = driver_object
        self.support = Support(self.driver)
        self.locators = {
            "add_beanie_to_cart_xpath":"//a[@data-product_sku='woo-beanie']",
            "cart_widget_id":"site-header-cart"
        }

    def click_add_beanie_to_cart(self):
        locator = self.locators['add_beanie_to_cart_xpath']
        self.support.click_button_found_by_xpath(locator)

    
    def hover_over_cart_widget(self):
        locator = self.locators['cart_widget_id']
        self.support.hover_over_elem_by_ID(locator)