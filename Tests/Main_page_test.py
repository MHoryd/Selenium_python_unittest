from selenium import webdriver
from Config.Test_settings import Test_settings_chrome_fabrykatestow_pl
from Pages_objects.Header_page import Header_page
from Pages_objects.Main_page import Main_Page
from Pages_objects.Product_page import Product_page
from Utilities.Support import Support
from Config.Test_data import Test_data
import unittest


class Main_page_test(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome(service=Test_settings_chrome_fabrykatestow_pl.chrome_service, options=Test_settings_chrome_fabrykatestow_pl.chrome_options)
        self.support = Support(self.driver)
        self.url = Test_settings_chrome_fabrykatestow_pl.url
        self.header_page_object = Header_page(self.driver)
        self.main_page_object = Main_Page(self.driver)
        self.product_page_object = Product_page(self.driver)
        self.driver.get(self.url)
        self.driver.maximize_window()
    
    def tearDown(self):
        self.driver.quit()



    def test1_main_page_new_category_header_and_item_are_displayed(self):
        self.assertTrue(self.main_page_object.new_category_group_is_displayed())
        self.assertTrue(self.main_page_object.item_in_new_category_group_is_displayed())


    def test2_main_page_favorite_category_header_and_item_are_displayed(self):
        self.assertTrue(self.main_page_object.favorite_category_group_is_displayed())
        self.assertTrue(self.main_page_object.item_in_favorite_category_group_is_displayed())

    
    def test3_main_page_bestseller_category_header_and_item_are_displayed(self):
        self.assertTrue(self.main_page_object.bestsellers_category_group_is_displayed())
        self.assertTrue(self.main_page_object.item_in_bestsellers_category_group_is_displayed())


    def test4_search_for_product_using_search_bar(self):
        self.header_page_object.insert_text_into_search_bar(Test_data.data['main_page_article'])
        self.header_page_object.submit_search_bar_input()
        self.assertEqual(self.product_page_object.get_product_name(),Test_data.data['main_page_article'])


    def test5_proper_price_is_displayed_for_product_in_stock(self):
        self.assertTrue(self.main_page_object.get_polo_price_from_new_category(),Test_data.data['main_page_article_price'])


if __name__ == '__main__':
    unittest.main()