from Utilities.Support import Support

class Cart_page():


    def __init__(self,driver_object):
        self.driver = driver_object
        self.support = Support(self.driver)
        self.locators = {
            "total_price_xpath":"//tr[@class='cart-subtotal']//bdi",
            "remove_cap_from_cart_buttom_xpath":"//a[@href='https://tapsshop.pl/?product=cap']/ancestor::tr//a[@class='remove']",
            "belt_product_page_link_xpath":"//td[@class='product-name']/a[@href='https://tapsshop.pl/?product=belt']"
        }


    def get_total_price(self):
        locator = self.locators['total_price_xpath']
        elem = self.support.get_elem(locator)
        return elem.text

    
    def click_remove_cap_buttom(self):
        locator = self.locators['remove_cap_from_cart_buttom_xpath']
        self.support.click_button_found_by_xpath(locator)


    def wait_untill_cap_will_be_removed(self):
        locator = self.locators['belt_product_page_link_xpath']
        self.support.wait_for_invisibility_of_elem_by_XPATH(locator)