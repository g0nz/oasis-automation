import unittest
from selenium import webdriver
from Pages.HomePage import *
from Pages.MailCheck import *

class booknow(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/Users/gonzaloroland/PycharmProjects/OasisAutomation/chromedriver')
        #self.driver.get('https://mail.google.com/?ui=html')
        self.mail_check = MailCheck(self.driver)

    def test_mailcheck(self):
        self.mail_check.open_mail()
        self.mail_check.login_mail()
