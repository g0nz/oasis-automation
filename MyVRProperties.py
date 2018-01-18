import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class AddProperty:

    def __init__(self, myDriver):
        self.driver = myDriver

    def myvr_login(self):
        driver = self.driver
        self.driver.get('https://myvr.com/')
        self.driver.find_element_by_xpath