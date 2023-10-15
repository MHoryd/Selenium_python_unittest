from Utilities.Support import Support


class Order_page():

    def __init__(self, driver_object):
        self.driver = driver_object
        self.support = Support(self.driver)
        self.locators = {
            "cart_is_empty_message_xpath":"//div[@class='cart-empty woocommerce-info']",
            "name_input_id":"billing_first_name",
            "surname_input_id":"billing_last_name",
            "country_dropdown_xpath":"//select",
            "street_input_id":"billing_address_1",
            "post_code_input_id":"billing_postcode",
            "city_input_id":"billing_city",
            "phone_input_id":"billing_phone",
            "email_input_id":"billing_email",
            "first_item_in_order_name_xpath":"//tr[@class='cart_item']/td[@class='product-name'][1]",
            "first_item_in_order_quantity_xpath":"//tr[@class='cart_item']/td[@class='product-name'][1]/strong",
            "first_item_in_order_price_xpath":"//tr[@class='cart_item']/td[@class='product-total'][1]/span/bdi",
            "order_total_price_xpath":"//tr[@class='order-total']//bdi",
            "place_order_button_id":"place_order",
            "order_placed_xpath":"//h1[contains(text(),'Zamówienie otrzymane')]",
            "order_number_xpath":"//li[@class='woocommerce-order-overview__order order']/strong",
            "order_total_price_in_checkout_xpath":"//ul[@class='woocommerce-order-overview woocommerce-thankyou-order-details order_details']//span[@class='woocommerce-Price-amount amount']//bdi",
            "checkout_is_processing_xpath":"//form[@class='checkout woocommerce-checkout processing']"
        }


    def assert_is_order_blank(self):
        locator = self.locators['cart_is_empty_message_xpath']
        return self.support.elem_is_displayed_found_by_xpath(locator)
    

    def insert_text_into_name_input(self,text):
        locator = self.locators['name_input_id']
        self.support.insert_text_into_input_found_by_ID(locator, text)


    def insert_text_into_surname_input(self,text):
        locator = self.locators['surname_input_id']
        self.support.insert_text_into_input_found_by_ID(locator, text)


    def insert_text_country_dropdown(self,text):
        locator = self.locators['country_dropdown_xpath']
        self.support.select_option_in_dropdown_by_text_elem_found_by_xpath(locator,text)


    def insert_text_into_street_input(self,text):
        locator = self.locators['street_input_id']
        self.support.insert_text_into_input_found_by_ID(locator, text)


    def insert_text_into_postcode_input(self,text):
        locator = self.locators['post_code_input_id']
        self.support.insert_text_into_input_found_by_ID(locator, text)


    def insert_text_into_city_input(self,text):
        locator = self.locators['city_input_id']
        self.support.insert_text_into_input_found_by_ID(locator, text)


    def insert_text_into_phone_input(self,text):
        locator = self.locators['phone_input_id']
        self.support.insert_text_into_input_found_by_ID(locator, text)


    def insert_text_into_email_input(self,text):
        locator = self.locators['email_input_id']
        self.support.insert_text_into_input_found_by_ID(locator, text)


    def get_first_item_in_order_name(self):
        locator = self.locators['first_item_in_order_name_xpath']
        return self.support.get_elem(locator).text
    

    def get_first_item_in_order_quantity(self):
        locator = self.locators['first_item_in_order_quantity_xpath']
        return self.support.get_elem(locator).text
    

    def get_first_item_in_order_price(self):
        locator = self.locators['first_item_in_order_price_xpath']
        return self.support.get_elem(locator).text
    

    def get_order_total_price(self):
        locator = self.locators['order_total_price_xpath']
        return self.support.get_elem(locator).text


    def assess_id_order_placed(self):
        locator = self.locators['order_placed_xpath']
        return self.support.elem_is_displayed_found_by_xpath(locator)
    

    def assess_is_order_number_displayed(self):
        locator = self.locators['order_number_xpath']
        return self.support.elem_is_displayed_found_by_xpath(locator)
    

    def get_order_total_price_in_checkout(self):
        locator = self.locators['order_total_price_in_checkout_xpath']
        return self.support.get_elem(locator).text
    

    def click_place_order_button(self):
        locator = self.locators['place_order_button_id']
        self.support.click_button_found_by_ID(locator)


    def wait_untill_order_in_placed(self):
        locator = self.locators['checkout_is_processing_xpath']
        self.support.wait_for_invisibility_of_elem_by_XPATH(locator)


    def hover_over_and_click_order_button(self):
        locator = self.locators['place_order_button_id']
        self.support.hover_over_elem_and_click_by_ID(locator)