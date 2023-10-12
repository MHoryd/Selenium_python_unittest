from selenium import webdriver
from Config.Test_settings import Test_settings_chrome_fabrykatestow_pl
from Utilities.Support import Support
from Pages_objects.Header_page import Header_page
from Pages_objects.Shop_page import Shop_page
from Config.Test_data import Test_data
import unittest, os, time



class Cart_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Test_settings_chrome_fabrykatestow_pl.chrome_service, options=Test_settings_chrome_fabrykatestow_pl.chrome_options)
        self.support = Support(self.driver)
        self.url = Test_settings_chrome_fabrykatestow_pl.url
        self.header_page = Header_page(self.driver)
        self.shop_page = Shop_page(self.driver)
        self.driver.get(self.url)
        self.driver.maximize_window()
    
    def tearDown(self):
        self.driver.quit()


    def test1_add_product_to_the_cart_and_check_widget_details(self):
        self.support.dismiss_initial_notice()
        self.header_page.click_shop_button()
        self.shop_page.click_add_beanie_to_cart()
        self.shop_page.hover_over_cart_widget()
        time.sleep(10)



    # def test2_add_multiple_the_same_products_to_the_cart_and_check_widget_details(self):
    #     pass


    # def test3_add_multiple_products_to_the_cart_and_check_widget_details(self):
    #     pass


    # def test4_add_multiple_products_to_the_cart_and_check_cart_page_details(self):
    #     pass


    # def test5_add_multiple_products_to_the_cart_remove_one_product_from_the_cart_widget_and_check_widget_details(self):
    #     pass


    # def test6_add_multiple_products_to_the_cart_remove_one_product_from_the_cart_page_and_check_page_details(self):
    #     pass


    # def test7_add_product_to_the_cart_and_change_product_amount_in_cart_page(self):
    #     pass    


    # def test8_add_multiple_products_to_the_cart_remove_all_product_from_the_cart_widget(self):
    #     pass    


    # def test9_add_multiple_products_to_the_cart_remove_all_product_from_the_cart_page(self):
    #     pass   


    # def test10_log_in_add_product_to_the_cart_and_check_cart_page_details(self):
    #     pass   


    # def test11_log_in_add_product_to_the_cart_log_out_log_in_and_check_is_product_still_in_cart(self):
    #     pass   


    # def test12_add_multiple_products_to_the_cart_from_product_page(self):
    #     pass  


if __name__ == '__main__':
    unittest.main()