import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class HomeSearch:

    def __init__(self, myDriver):
        self.driver = myDriver

    def homepage_search(self):
        driver = self.driver
        driver.get('https://stage.oasiscollections.com/')
        driver.implicitly_wait(15)
        #time.sleep(5)
        destination_dropdown = driver.find_element_by_xpath(
            '/html/body/div[2]/section/div/div/div/section[1]/div[2]/home-search-bar/div/div[1]')
        destination_dropdown.click()
        destination_destination = driver.find_element_by_xpath(
            '/html/body/div[2]/section/div/div/div/section[1]/div[2]/home-search-bar/div/div[1]/div/div/div/div/div[2]/div[16]/label')
        destination_destination.click()
        date_picker = driver.find_element_by_xpath(
            '/html/body/div[2]/section/div/div/div/section[1]/div[2]/home-search-bar/div/div[2]/oasis-date-range-picker/div[1]/div[1]')
        date_picker.click()
        arrow = driver.find_element_by_xpath('/html/body/div[2]/section/div/div/div/section[1]/div[2]/home-search-bar/div/div[2]/oasis-date-range-picker/div[2]/oasis-date-picker-visor/div[1]/span[2]')
        arrow.click()
        arrow.click()
        arrow.click()
        arrow.click()
        date_in = driver.find_element_by_xpath(
            '/html/body/div[2]/section/div/div/div/section[1]/div[2]/home-search-bar/div/div[2]/oasis-date-range-picker/div[2]/oasis-date-picker-visor/div[1]/div/div[3]/oasis-date-picker/table/tbody/tr[1]/td[5]')
        date_in.click()
        date_out = driver.find_element_by_xpath(
            '/html/body/div[2]/section/div/div/div/section[1]/div[2]/home-search-bar/div/div[2]/oasis-date-range-picker/div[2]/oasis-date-picker-visor/div[1]/div/div[3]/oasis-date-picker/table/tbody/tr[2]/td[5]')
        date_out.click()
        search_button = driver.find_element_by_xpath(
            '/html/body/div[2]/section/div/div/div/section[1]/div[2]/home-search-bar/div/div[4]')
        search_button.click()
        #time.sleep(10)

    def pageresult_select(self):
        driver = self.driver
        driver.implicitly_wait(15)
        window_before = driver.window_handles[0]
        first_result = driver.find_element_by_xpath(
            '/html/body/div[2]/section/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/a[1]')
        first_result.click()
        window_after = driver.window_handles[1]
        #time.sleep(10)
        driver.switch_to.window(window_after)
        booknow_button = driver.find_element_by_xpath(
            '//*[@id="details"]/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/div[1]/button')
        #time.sleep(5)
        booknow_button.send_keys(Keys.SPACE)
        #time.sleep(5)
        #date_in_b = driver.find_element_by_xpath('//*[@id="details"]/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div[1]/div/oasis-date-range-picker/div[2]/oasis-date-picker-visor/div[1]/div/div[2]/oasis-date-picker/table/tbody/tr[4]/td[6]')
        #date_in_b.click()
        #date_out_b = driver.find_element_by_xpath('//*[@id="details"]/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/div[1]/div/oasis-date-range-picker/div[2]/oasis-date-picker-visor/div[1]/div/div[2]/oasis-date-picker/table/tbody/tr[5]/td[4]')
        #date_out_b.click()
        #booknow_button.send_keys(Keys.SPACE)
        #time.sleep(10)

    def payment_flow(self):
        driver = self.driver
        driver.implicitly_wait(15)
        card_number_field = driver.find_element_by_xpath('//*[@id="bookNowForm"]/div[2]/div[2]/input')
        card_number_field.send_keys('4242424242424242')
        cardholder_name_field = driver.find_element_by_xpath('//*[@id="bookNowForm"]/div[2]/div[4]/input')
        cardholder_name_field.send_keys('Test Name')
        exp_date_dield = driver.find_element_by_xpath('//*[@id="bookNowForm"]/div[2]/div[5]/div[1]/input')
        exp_date_dield.send_keys('042020')
        cvv_field = driver.find_element_by_xpath('//*[@id="bookNowForm"]/div[2]/div[5]/div[2]/input')
        cvv_field.send_keys('123')
        zip_field = driver.find_element_by_xpath('//*[@id="bookNowForm"]/div[2]/div[5]/div[3]/input')
        zip_field.send_keys('90210')
        firstname_field = driver.find_element_by_xpath('//*[@id="bookNowForm"]/div[3]/div[2]/div[1]/div[1]/input')
        firstname_field.send_keys('Test Name')
        lastname_field = driver.find_element_by_xpath('//*[@id="bookNowForm"]/div[3]/div[2]/div[2]/div[1]/input')
        lastname_field.send_keys('Test Surname')
        email_field = driver.find_element_by_xpath('//*[@id="bookNowForm"]/div[3]/div[2]/div[1]/div[2]/input')
        email_field.send_keys('gonzalo@oasiscollection.com')
        guests_dropdown = Select(driver.find_element_by_xpath('//*[@id="number-of-guests"]'))
        guests_dropdown.select_by_visible_text('5')
        countrycode_dropdown = Select(driver.find_element_by_xpath('//*[@id="country-code"]'))
        countrycode_dropdown.select_by_visible_text('United States (+1)')
        phonenumber_field = driver.find_element_by_xpath('//*[@id="bookNowForm"]/div[3]/div[3]/div[2]/input')
        phonenumber_field.send_keys('6666666')
        comments_field = driver.find_element_by_xpath('//*[@id="bookNowForm"]/div[3]/div[4]/div[1]/textarea')
        comments_field.send_keys('This is a test comment')
        terms_checkbox = driver.find_element_by_xpath('//*[@id="bookNowForm"]/div[3]/div[4]/div[2]/div[2]/label[1]')
        terms_checkbox.click()
        #time.sleep(10)
        confirm_button = driver.find_element_by_xpath('//*[@id="bookNowForm"]/div[3]/div[4]/div[2]/div[1]/button')
        confirm_button.click()
        #time.sleep(30)

