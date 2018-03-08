import unittest
from Pages.HomePage import *
from Pages.MailCheck import *
from Pages.MyVRPayment import *
from Pages.MyVRCheck import *

class booknow(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/Users/gonzaloroland/PycharmProjects/OasisAutomationFramework/chromedriver')
        self.home_search = HomeSearch(self.driver)
        self.mail_check = MailCheck(self.driver)
        self.myvr_pay = MyVRPayment(self.driver)
        self.myvr_check = CheckInfo(self.driver)

    def test_book(self):
        self.home_search.homepage_search()
        self.home_search.pageresult_booknow()
        self.home_search.inquiry_fill()
        self.myvr_pay.myvrpayment()

    def test_infocheck(self):
        self.mail_check.open_mail()
        self.mail_check.login_mail('gonzalo@oasiscollections.com', 'Pungahijodeputa87')
        self.mail_check.check_res_data()
        self.myvr_check.myvr_login()
        self.myvr_check.myvr_reservation()
        assert date_in_slice == date_in_myvr
        assert date_out_slice == date_out_myvr

    def tearDown(self):
        self.driver.quit()