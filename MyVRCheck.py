import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class CheckInfo:

    def __init__(self, myDriver):
        self.driver = myDriver

    def myvr_login(self):
        self.driver.get('https://myvr.com/')
        self.driver.find_element_by_xpath('//*[@id="myvr-collapse"]/ul/li[6]').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//*[@id="body"]/div/div/div/div/form/div[1]/input').send_keys('gonzalo@oasiscollections.com', Keys.TAB, 'Pungahijodeputa87', Keys.ENTER)
        time.sleep(5)

    def myvr_reservation(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath('//*[@id="side-menu"]/li[9]').click()
        self.driver.find_element_by_xpath('//*[@id="side-menu"]/li[9]/ul/li[1]').click()
        self.driver.find_element_by_xpath('//*[@id="reservationDetails"]/table/tbody/tr[1]/td[3]').click()
        time.sleep(10)
        date_in_myvr = (self.driver.find_element_by_xpath('//*[@id="page-wrapper"]/div[2]/div[7]/div/div/div/div[24]/div[2]/div/div[1]/div[2]/fieldset/div/div[2]/table/tbody/tr[1]/td[2]')).text
        date_out_myvr = (self.driver.find_element_by_xpath('//*[@id="page-wrapper"]/div[2]/div[7]/div/div/div/div[24]/div[2]/div/div[1]/div[2]/fieldset/div/div[2]/table/tbody/tr[2]/td[2]')).text
        print date_in_myvr
        print date_out_myvr

    def myvr_inquiry(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath('')
        date_in_myvr_i = self.driver.find_element_by_xpath('//*[@id="inquiryDetail"]/div/div[2]/fieldset/div/div[2]/table/tbody/tr[1]/td[2]')
        date_out_myvr_i = self.driver.find_element_by_xpath('//*[@id="inquiryDetail"]/div/div[2]/fieldset/div/div[2]/table/tbody/tr[2]/td[2]')
