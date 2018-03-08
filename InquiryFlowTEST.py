import unittest
from Pages.HomePage import *
from Pages.MailCheck import *
from Pages.MyVRPayment import *


class booknow(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/Users/gonzaloroland/PycharmProjects/OasisAutomationFramework/chromedriver')
        self.home_search = HomeSearch(self.driver)
        self.mail_check = MailCheck(self.driver)
        self.myvr_pay = MyVRPayment(self.driver)

    def test_inquiry(self):
        self.home_search.homepage_search()
        self.home_search.pageresult_inquiry()
        self.home_search.inquiry_fill()
        self.myvr_pay.myvrpayment()

    def test_mailcheck(self):
        self.mail_check.open_mail()
        self.mail_check.login_mail('gonzalo@oasiscollections.com', 'Pungahijodeputa87')
        #checkinquiry
        self.mail_check.check_res_data()

    def tearDown(self):
        self.driver.quit()