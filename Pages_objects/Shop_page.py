from Utilities.Support import Support

class Shop_page():


    def __init__(self,driver_object):
        self.driver = driver_object
        self.support = Support(self.driver)
        self.locators = {
            "Add_beanie_to_cart_xpath":"//a[@data-product_sku='woo-beanie']"
        }

    def click_add_beanie_to_cart(self):
        locator = self.locators['Add_beanie_to_cart_xpath']
        self.support.click_button_found_by_xpath(locator)