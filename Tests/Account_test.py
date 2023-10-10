from selenium import webdriver
from Config.Test_settings import Test_settings_chrome_fabrykatestow_pl
from Pages_objects.My_account_page import My_account_page
from Pages_objects.Header_page import Header_page
from Utilities.Support import Support
import unittest, os, time


class Account_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Test_settings_chrome_fabrykatestow_pl.chrome_service, options=Test_settings_chrome_fabrykatestow_pl.chrome_options)
        self.support = Support(self.driver)
        self.header_page = Header_page(self.driver,self.support)
        self.my_account_page = My_account_page(self.driver,self.support)
        self.url = Test_settings_chrome_fabrykatestow_pl.url
        self.driver.get(self.url)
        self.driver.maximize_window()
    
    def tearDown(self):
        self.driver.quit()


    def test1_register_using_random_email(self):
        self.support.dismiss_initial_notice()
        self.header_page.click_my_account_button()
        self.my_account_page.insert_text_into_registration_input(self.support.get_random_email())
        self.my_account_page.click_registration_button()
        self.assertTrue(self.my_account_page.log_in_is_successful())


    def test2_log_in_using_invalid_email(self):
        self.support.dismiss_initial_notice()
        self.header_page.click_my_account_button()
        self.my_account_page.insert_text_into_log_in_email_input('aaa')
        self.my_account_page.insert_text_into_log_in_password_input('sss')
        self.my_account_page.click_log_in_button()
        self.assertEqual(self.my_account_page.get_invalid_both_credentials_error(),'BŁĄD: nieprawidłowa nazwa użytkownika lub hasło.')


    def test3_log_in_using_valid_email_and_log_off(self):
        self.support.dismiss_initial_notice()
        self.header_page.click_my_account_button()
        self.my_account_page.insert_text_into_log_in_email_input(os.environ.get('tapsshop_proper_email'))
        self.my_account_page.insert_text_into_log_in_password_input(os.environ.get('tapsshop_proper_password'))
        self.my_account_page.click_log_in_button()
        self.assertTrue(self.my_account_page.log_in_is_successful())
        self.my_account_page.click_log_out_button()
        self.assertTrue(self.my_account_page.log_out_is_successful())


    def test4_edit_billing_address(self):
        self.support.dismiss_initial_notice()
        self.header_page.click_my_account_button()
        self.my_account_page.insert_text_into_log_in_email_input(os.environ.get('tapsshop_proper_email'))
        self.my_account_page.insert_text_into_log_in_password_input(os.environ.get('tapsshop_proper_password'))
        self.my_account_page.click_log_in_button()
        self.my_account_page.click_address_nav_button()
        self.my_account_page.click_edit_address_button()
        self.my_account_page.select_value_in_address_country_dropdown('Polska')
        self.my_account_page.clear_text_in_billing_street_input()
        self.my_account_page.clear_text_in_billing_postal_code_input()
        self.my_account_page.clear_text_in_billing_city_input()
        self.my_account_page.clear_text_in_billing_phone_input()
        self.my_account_page.insert_text_into_billing_street_input('Testowa')
        self.my_account_page.insert_text_into_billing_postal_code_input('11-111')
        self.my_account_page.insert_text_into_billing_city_input('Test')
        self.my_account_page.insert_text_into_billing_phone_input('123456789')
        self.my_account_page.click_save_billing_address_button()
        self.assertEqual(self.my_account_page.check_is_new_billing_adress_valid(),"Adam Test\nTestowa\n11-111 Test")

        



if __name__ == '__main__':
    unittest.main()