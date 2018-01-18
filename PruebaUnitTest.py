import unittest
from selenium import webdriver
from Pages.HomePage import *
from Pages.MailCheck import *

class booknow(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/Users/gonzaloroland/PycharmProjects/OasisAutomation/chromedriver')
        self.home_search = HomeSearch(self.driver)
        self.mail_check = MailCheck(self.driver)

    def test_book(self):
        self.home_search.homepage_search()
        self.home_search.pageresult_select()
        self.home_search.payment_flow()

    def test_mailcheck(self):
        self.mail_check.open_mail()

    def tearDown(self):
        self.driver.quit()