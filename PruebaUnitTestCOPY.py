import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

class booknow(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/Users/gonzaloroland/PycharmProjects/OasisAutomation/chromedriver')

    def test_book(self):
        driver = self.driver
        driver.get('https://www.oasiscollections.com/')
        time.sleep(5)
        destination_dropdown = driver.find_element_by_xpath(
            '/html/body/div[2]/section/div/div/div/section[1]/div[2]/home-search-bar/div/div[1]')
        destination_dropdown.click()
        destination_destination = driver.find_element_by_xpath(
            '/html/body/div[2]/section/div/div/div/section[1]/div[2]/home-search-bar/div/div[1]/div/div/div/div/div[2]/div[1]/label')
        destination_destination.click()
        date_picker = driver.find_element_by_xpath(
            '/html/body/div[2]/section/div/div/div/section[1]/div[2]/home-search-bar/div/div[2]/oasis-date-range-picker/div[1]/div[1]')
        date_picker.click()
        date_in = driver.find_element_by_xpath(
            '/html/body/div[2]/section/div/div/div/section[1]/div[2]/home-search-bar/div/div[2]/oasis-date-range-picker/div[2]/oasis-date-picker-visor/div[1]/div/div[2]/oasis-date-picker/table/tbody/tr[5]/td[7]/span')
        date_in.click()
        date_out = driver.find_element_by_xpath(
            '/html/body/div[2]/section/div/div/div/section[1]/div[2]/home-search-bar/div/div[2]/oasis-date-range-picker/div[2]/oasis-date-picker-visor/div[1]/div/div[3]/oasis-date-picker/table/tbody/tr[1]/td[7]/span')
        date_out.click()
        search_button = driver.find_element_by_xpath(
            '/html/body/div[2]/section/div/div/div/section[1]/div[2]/home-search-bar/div/div[4]')
        search_button.click()
        time.sleep(5)
        window_before = driver.window_handles[0]
        first_result = driver.find_element_by_xpath(
            '/html/body/div[2]/section/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/a[1]/div')
        first_result.click()
        window_after = driver.window_handles[1]
        time.sleep(5)
        driver.switch_to.window(window_after)
        booknow_button = driver.find_element_by_xpath(
            '//*[@id="details"]/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/div[1]/button')
        time.sleep(5)
        booknow_button.send_keys(Keys.SPACE)

    def tearDown(self):
        self.driver.quit()