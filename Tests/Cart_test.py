from selenium import webdriver
from Config.Test_settings import Test_settings_chrome_fabrykatestow_pl
from Utilities.Support import Support
from Pages_objects.Header_page import Header_page
from Pages_objects.Shop_page import Shop_page
from Pages_objects.Cart_page import Cart_page
from Pages_objects.My_account_page import My_account_page
from Config.Test_data import Test_data
import unittest, os, time



class Cart_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Test_settings_chrome_fabrykatestow_pl.chrome_service, options=Test_settings_chrome_fabrykatestow_pl.chrome_options)
        self.support = Support(self.driver)
        self.url = Test_settings_chrome_fabrykatestow_pl.url
        self.header_page = Header_page(self.driver)
        self.shop_page = Shop_page(self.driver)
        self.cart_page = Cart_page(self.driver)
        self.my_account_page = My_account_page(self.driver)
        self.driver.get(self.url)
        self.driver.maximize_window()
    
    def tearDown(self):
        self.driver.quit()


    def test1_add_product_to_the_cart_and_check_widget_details(self):
        self.support.dismiss_initial_notice()
        self.header_page.click_shop_button()
        self.shop_page.click_add_beanie_to_cart()
        self.assertEqual(self.shop_page.get_product_in_cart_count(),1)
        self.shop_page.hover_over_cart_widget()
        self.assertEqual(self.shop_page.get_total_price_from_cart_widget(), Test_data.data['beanie_single_item_in_cart_price'])
        


    def test2_add_multiple_the_same_products_to_the_cart_and_check_widget_details(self):
        self.support.dismiss_initial_notice()
        self.header_page.click_shop_button()
        for i in range(3):
            self.shop_page.click_add_beanie_to_cart()
            self.shop_page.wait_for_products_to_be_loaded_to_cart_after_button_click()
        self.assertEqual(self.shop_page.get_product_in_cart_count(),3)
        self.shop_page.hover_over_cart_widget()
        self.assertEqual(self.shop_page.get_total_price_from_cart_widget(),Test_data.data['beanie_three_item_in_cart_price'])


    def test3_add_multiple_products_to_the_cart_and_check_widget_details(self):
        self.support.dismiss_initial_notice()
        self.header_page.click_shop_button()
        self.shop_page.click_add_beanie_to_cart()
        self.shop_page.click_add_belt_to_cart()
        self.shop_page.click_add_cap_to_cart()
        self.shop_page.wait_for_products_to_be_loaded_to_cart_after_button_click()
        self.assertEqual(self.shop_page.get_product_in_cart_count(),3)
        self.shop_page.hover_over_cart_widget()
        self.assertEqual(self.shop_page.get_total_price_from_cart_widget(),Test_data.data['beanie_belt_cap_items_in_cart_price'])


    def test4_add_multiple_products_to_the_cart_and_check_cart_page_details(self):
        self.support.dismiss_initial_notice()
        self.header_page.click_shop_button()
        self.shop_page.click_add_beanie_to_cart()
        self.shop_page.click_add_belt_to_cart()
        self.shop_page.click_add_cap_to_cart()
        self.shop_page.wait_for_products_to_be_loaded_to_cart_after_button_click()
        self.shop_page.hover_over_cart_widget()
        self.shop_page.click_cart_page_button_from_widget()
        self.assertEqual(self.cart_page.get_total_price(),Test_data.data['beanie_belt_cap_items_in_cart_price'])


    def test5_add_multiple_products_to_the_cart_remove_one_product_from_the_cart_widget_and_check_widget_details(self):
        self.support.dismiss_initial_notice()
        self.header_page.click_shop_button()
        self.shop_page.click_add_beanie_to_cart()
        self.shop_page.click_add_belt_to_cart()
        self.shop_page.click_add_cap_to_cart()
        self.shop_page.wait_for_products_to_be_loaded_to_cart_after_button_click()
        self.shop_page.hover_over_cart_widget()
        self.shop_page.click_remove_cap_from_cart_in_widget()
        self.shop_page.wait_for_cap_to_be_removed_from_widget()
        self.assertEqual(self.shop_page.get_total_price_from_cart_widget(),Test_data.data['beanie_belt_items_in_cart_price'])


    def test6_add_multiple_products_to_the_cart_remove_one_product_from_the_cart_page_and_check_page_details(self):
        self.support.dismiss_initial_notice()
        self.header_page.click_shop_button()
        self.shop_page.click_add_beanie_to_cart()
        self.shop_page.click_add_belt_to_cart()
        self.shop_page.click_add_cap_to_cart()
        self.shop_page.wait_for_products_to_be_loaded_to_cart_after_button_click()
        self.shop_page.hover_over_cart_widget()
        self.shop_page.click_cart_page_button_from_widget()
        self.cart_page.click_remove_cap_buttom()
        self.cart_page.wait_untill_cap_will_be_removed()
        self.assertEqual(self.cart_page.get_total_price(),Test_data.data['beanie_belt_items_in_cart_price'])


    def test7_add_product_to_the_cart_and_change_product_amount_in_cart_page(self):
        self.support.dismiss_initial_notice()
        self.header_page.click_shop_button()
        self.shop_page.click_add_beanie_to_cart()
        self.shop_page.wait_for_products_to_be_loaded_to_cart_after_button_click()
        self.shop_page.hover_over_cart_widget()
        self.shop_page.click_cart_page_button_from_widget()
        self.cart_page.clear_beanie_quantity_input()
        self.cart_page.insert_new_beanie_quantity(Test_data.data['beanie_new_quantity_for_cart_page_test'])
        self.cart_page.update_cart()
        self.cart_page.wait_untill_cart_is_updated()
        self.assertEqual(self.cart_page.get_total_price(),Test_data.data['beanie_new_quantity_for_cart_page_test_expected_total_price'])


    def test8_add_multiple_products_to_the_cart_remove_all_product_from_the_cart_widget(self):
        self.support.dismiss_initial_notice()
        self.header_page.click_shop_button()
        self.shop_page.click_add_beanie_to_cart()
        self.shop_page.click_add_belt_to_cart()
        self.shop_page.click_add_cap_to_cart()
        self.shop_page.wait_for_products_to_be_loaded_to_cart_after_button_click()
        self.shop_page.hover_over_cart_widget()
        self.shop_page.click_remove_cap_from_cart_in_widget()   
        self.shop_page.click_remove_beanie_from_cart_in_widget()
        self.shop_page.click_remove_belt_from_cart_in_widget()
        self.shop_page.hover_over_cart_widget()
        self.assertTrue(self.shop_page.assess_is_cart_empty())


    def test9_add_multiple_products_to_the_cart_remove_all_product_from_the_cart_page(self):
        self.support.dismiss_initial_notice()
        self.header_page.click_shop_button()
        self.shop_page.click_add_beanie_to_cart()
        self.shop_page.click_add_belt_to_cart()
        self.shop_page.click_add_cap_to_cart()
        self.shop_page.wait_for_products_to_be_loaded_to_cart_after_button_click()
        self.shop_page.hover_over_cart_widget()   
        self.shop_page.click_cart_page_button_from_widget()
        self.cart_page.click_remove_beanie_buttom()
        self.cart_page.wait_untill_beanie_will_be_removed()
        self.cart_page.click_remove_belt_buttom()
        self.cart_page.wait_untill_belt_will_be_removed()
        self.cart_page.click_remove_cap_buttom()
        self.cart_page.wait_untill_cap_will_be_removed()
        self.assertTrue(self.cart_page.assess_is_cart_empty())


    def test10_log_in_add_product_to_the_cart_and_check_cart_page_details(self):
        self.support.dismiss_initial_notice()
        self.header_page.click_my_account_button()
        self.my_account_page.insert_text_into_log_in_email_input(os.environ.get('tapsshop_proper_email'))
        self.my_account_page.insert_text_into_log_in_password_input(os.environ.get('tapsshop_proper_password'))
        self.my_account_page.click_log_in_button()
        self.my_account_page.log_in_is_successful()
        self.support.delete_all_cart_cookies()
        self.header_page.click_shop_button()
        self.support.print_cookies()
        self.driver.refresh
        self.shop_page.click_add_beanie_to_cart()
        self.assertEqual(self.shop_page.get_product_in_cart_count(),1)
        self.shop_page.hover_over_cart_widget()
        self.assertEqual(self.shop_page.get_total_price_from_cart_widget(), Test_data.data['beanie_single_item_in_cart_price'])

    # def test11_log_in_add_product_to_the_cart_log_out_log_in_and_check_is_product_still_in_cart(self):
    #     pass   


    # def test12_add_multiple_products_to_the_cart_from_product_page(self):
    #     pass  


if __name__ == '__main__':
    unittest.main()