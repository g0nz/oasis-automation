import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class propertyaddition(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/Users/gonzaloroland/PycharmProjects/OasisAutomation/chromedriver')

    def test_login(self):
        self.driver.get('https://myvr.com/')
        self.driver.find_element_by_xpath('//*[@id="myvr-collapse"]/ul/li[6]').click()
        self.driver.find_element_by_xpath('//*[@id="body"]/div/div/div/div/form/div[1]/input').send_keys('gonzalo@oasiscollections.com', Keys.TAB, 'Pungahijodeputa87', Keys.ENTER)
