from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class Test_settings_chrome_fabrykatestow_pl:


    url = 'https://tapsshop.pl/'
    chrome_binary_path  = 'Browsers\Chrome\chrome.exe'
    chrome_driver_path  = "Drivers\chromedriver.exe"
    chrome_options = Options()
    chrome_options.binary_location = chrome_binary_path
    chrome_service = Service(chrome_driver_path)