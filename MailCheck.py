import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class MailCheck:

    def __init__(self, myDriver):
        self.driver = myDriver
        #self.email_field = self.driver.find_element_by_xpath('//*[@id="identifierId"]')
        #self.next_button = self.driver.find_element_by_xpath('//*[@id="identifierNext"]')
        #self.pass_field = self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        #self.conf_user = self.driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/form/table[2]/tbody/tr[1]/td[3]/a')

    def open_mail(self):
        self.driver.get('https://mail.google.com/?ui=html')
        self.driver.implicitly_wait(5)

    def login_mail(self):
        self.driver
        self.driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys('gonzalo@oasiscollections.com')
        self.driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys('Pungahijodeputa87', Keys.ENTER)
        #self.driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/form/table[2]/tbody/tr[1]/td[3]/a').click()
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(By.XPATH('')))
        #pass_field.click().send_keys('Pungahijodeputa87')


