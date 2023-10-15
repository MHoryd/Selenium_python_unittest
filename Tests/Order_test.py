from selenium import webdriver
from Config.Test_settings import Test_settings_chrome_fabrykatestow_pl
from Pages_objects.Shop_page import Shop_page
from Pages_objects.Header_page import Header_page
from Pages_objects.Product_page import Product_page
from Pages_objects.My_account_page import My_account_page
from Pages_objects.Order_page import Order_page
from Utilities.Support import Support
from Config.Test_data import Test_data
import unittest, os


class Order_test(unittest.TestCase):



    def setUp(self):
        self.driver = webdriver.Chrome(service=Test_settings_chrome_fabrykatestow_pl.chrome_service, options=Test_settings_chrome_fabrykatestow_pl.chrome_options)
        self.support = Support(self.driver)
        self.url = Test_settings_chrome_fabrykatestow_pl.url
        self.header_page = Header_page(self.driver)
        self.shop_page = Shop_page(self.driver)
        self.cart_page = Header_page(self.driver)
        self.product_page = Product_page(self.driver)
        self.my_account_page = My_account_page(self.driver)
        self.order_page = Order_page(self.driver)
        self.driver.get(self.url)
        self.driver.maximize_window()
    

    def tearDown(self):
        self.driver.quit()


    def test1_Order_page_is_empty_when_cart_is_empty_being_log_off(self):
        self.support.dismiss_initial_notice()
        self.header_page.click_order_button()
        self.assertTrue(self.order_page.assert_is_order_blank())
        

    def test2_Order_page_is_empty_when_cart_is_empty_beign_log_in(self):
        self.support.dismiss_initial_notice()
        self.header_page.click_my_account_button()
        self.my_account_page.insert_text_into_log_in_email_input(os.environ.get('tapsshop_proper_email'))
        self.my_account_page.insert_text_into_log_in_password_input(os.environ.get('tapsshop_proper_password'))
        self.my_account_page.click_log_in_button()
        self.header_page.click_order_button()
        self.assertTrue(self.order_page.assert_is_order_blank())


    def test3_Order_item_being_log_off(self):
        self.support.dismiss_initial_notice()
        self.header_page.click_shop_button()
        self.shop_page.click_add_beanie_to_cart()
        self.shop_page.wait_for_products_to_be_loaded_to_cart_after_button_click()
        self.header_page.click_order_button()
        self.order_page.insert_text_into_email_input(os.environ.get('tapsshop_proper_email'))
        self.order_page.insert_text_into_postcode_input(Test_data.data['billing_address_postal_code'])
        self.order_page.insert_text_into_name_input(Test_data.data['test_account_name'])
        self.order_page.insert_text_into_surname_input(Test_data.data['test_account_surname'])
        self.order_page.insert_text_country_dropdown(Test_data.data['billing_address_country_dropdown_value'])
        self.order_page.insert_text_into_street_input(Test_data.data['billing_address_street'])
        self.order_page.insert_text_into_city_input(Test_data.data['billing_address_city'])
        self.order_page.insert_text_into_phone_input(Test_data.data['billing_address_phone'])
        self.order_page.hover_over_and_click_order_button()
        self.order_page.wait_untill_order_in_placed()
        self.assertTrue(self.order_page.assess_id_order_placed())
        self.assertTrue(self.order_page.assess_is_order_number_displayed())
        self.assertEqual(self.order_page.get_order_total_price_in_checkout(),Test_data.data['test_order_total_price'])


    def test4_Order_item_being_log_in(self):
        self.support.dismiss_initial_notice()
        self.header_page.click_my_account_button()
        self.my_account_page.insert_text_into_log_in_email_input(os.environ.get('tapsshop_proper_email'))
        self.my_account_page.insert_text_into_log_in_password_input(os.environ.get('tapsshop_proper_password'))
        self.my_account_page.click_log_in_button()
        self.header_page.click_shop_button()
        self.shop_page.click_add_beanie_to_cart()
        self.shop_page.wait_for_products_to_be_loaded_to_cart_after_button_click()
        self.header_page.click_order_button()
        self.order_page.hover_over_and_click_order_button()
        self.assertTrue(self.order_page.assess_id_order_placed())
        self.assertTrue(self.order_page.assess_is_order_number_displayed())
        self.assertEqual(self.order_page.get_order_total_price_in_checkout(),Test_data.data['test_order_total_price'])


if __name__ == '__main__':
    unittest.main()