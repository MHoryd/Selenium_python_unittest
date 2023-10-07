class Product_page():


    def __init__(self, driver_object, support_object):
        self.driver = driver_object
        self.support = support_object
        self.locators = {
            "product_title":"//h1[@class='product_title entry-title']"
        }

    def elem_is_displayed(self, locator):
        elem = self.support.wait_for_visibility_of_elem_by_XPATH(locator)
        return elem.is_displayed()
    
    
    def get_elem(self, locator):
        elem = self.support.wait_for_visibility_of_elem_by_XPATH(locator)
        return elem
    



    def get_product_name(self):
        locator = self.locators['product_title']
        elem = self.get_elem(locator)
        return elem.text
