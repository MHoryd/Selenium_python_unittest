class Home_page():

    def __init__(self, driver_object, support_object):
        self.driver = driver_object
        self.support = support_object
        self.locators = {
            "main_logo":"//a/img[@class='custom-logo']"
        }
    

    def elem_is_displayed(self, locator):
        elem = self.support.wait_for_visibility_of_elem_by_XPATH(locator)
        return elem.is_displayed()



    def is_main_page_displayed(self):
        locator = self.locators["main_logo"]
        return self.elem_is_displayed(locator)