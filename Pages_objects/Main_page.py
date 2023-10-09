class Main_Page():


    def __init__(self, driver_object,support_object):
        self.driver = driver_object
        self.support = support_object
        self.locators = {
            "new_category_xpath":"//h2[contains(text(),'Nowe')]",
            "favorite_category_xpath":"//h2[contains(text(),'Ulubione')]",
            "bestsellers_category_xpath":"//h2[contains(text(),'Bestsellery')]",
            "first_product_from_new_category_xpath":"//div[@class='entry-content']/div[3]/ul/li[1]",
            "first_product_from_favorite_category_xpath":"//div[@class='entry-content']/div[4]/ul/li[1]",
            "first_product_from_bestsellers_category_xpath":"//div[@class='entry-content']/div[5]/ul/li[1]",
            "price_of_polo_from_new_categoty_xpath":"//div[@class='entry-content']/div[3]//div[contains(text(),'Polo')]/../../div[1]/span"
        }



    def new_category_group_is_displayed(self):
        locator = self.locators['new_category_xpath']
        return self.support.elem_is_displayed(locator)
    
    def item_in_new_category_group_is_displayed(self):
        locator = self.locators['first_product_from_new_category_xpath']
        return self.support.elem_is_displayed(locator)
    

    def favorite_category_group_is_displayed(self):
        locator = self.locators['favorite_category_xpath']
        return self.support.elem_is_displayed(locator)
    

    def item_in_favorite_category_group_is_displayed(self):
        locator = self.locators['first_product_from_favorite_category_xpath']
        return self.support.elem_is_displayed(locator)
    

    def bestsellers_category_group_is_displayed(self):
        locator = self.locators['bestsellers_category_xpath']
        return self.support.elem_is_displayed(locator)
    

    def item_in_bestsellers_category_group_is_displayed(self):
        locator = self.locators['first_product_from_bestsellers_category_xpath']
        return self.support.elem_is_displayed(locator)
    

    def get_polo_price_from_new_category(self):
        locator = self.locators['price_of_polo_from_new_categoty_xpath']
        elem = self.support.get_elem(locator)
        return elem.text