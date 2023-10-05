from selenium import webdriver
from Config.Test_settings import Test_settings_chrome_fabrykatestow_pl
from Pages_objects.Home_page import Home_page
from Utilities.Support import Support
import unittest


class Page_test(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome(service=Test_settings_chrome_fabrykatestow_pl.chrome_service, options=Test_settings_chrome_fabrykatestow_pl.chrome_options)
        self.support = Support(self.driver)
        self.url = Test_settings_chrome_fabrykatestow_pl.url
        self.home_page_object = Home_page(self.driver,self.support)
        self.driver.get(self.url)
        self.driver.maximize_window()
    
    def tearDown(self):
        self.driver.quit()



    def test1(self):
        self.assertTrue(self.home_page_object.is_main_page_displayed())


if __name__ == '__main__':
    unittest.main()