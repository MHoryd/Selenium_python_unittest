from selenium import webdriver
from Config.Test_settings import Test_settings_chrome_fabrykatestow_pl
from Utilities.Support import Support
import unittest


class Page_test(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome(service=Test_settings_chrome_fabrykatestow_pl.chrome_service, options=Test_settings_chrome_fabrykatestow_pl.chrome_options)
        self.support = Support(self.driver)
        self.url = Test_settings_chrome_fabrykatestow_pl.url
        self.driver.get(self.url)
        self.driver.maximize_window()
    
    def tearDown(self):
        self.driver.quit()



    def test1(self):
        self.support.wait_for_visibility_of_elem_by_ID('test')


if __name__ == '__main__':
    unittest.main()