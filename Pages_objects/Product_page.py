from Utilities.Support import Support

class Product_page():


    def __init__(self, driver_object):
        self.driver = driver_object
        self.support = Support(self.driver)
        self.locators = {
            "product_title":"//h1[@class='product_title entry-title']"
        }


    def get_product_name(self):
        locator = self.locators['product_title']
        elem = self.support.get_elem(locator)
        return elem.text
