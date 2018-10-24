from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


class CandidatesList:
    def sortby_name(self):
        baseurl = 'https://candidx.io/'
        driver = webdriver.Chrome()
        # options.add_argument('--disable-extensions')
        # options.add_argument('--disable-gpu')
        # options.add_argument('--no-sandbox')
        driver.get(baseurl)
        driver.implicitly_wait(5)

        username_input = driver.find_element_by_name('userEmail')
        username_input.send_keys('amratest')

        password_input = driver.find_element_by_name('userPassword')
        password_input.send_keys('iQwuVCtqHQ1juU3')

        login_click = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[2]/div[3]/div[1]/div/div')
        login_click.click()
        time.sleep(2)

        menu_selection = driver.find_element_by_tag_name('svg')
        menu_selection.click()
        time.sleep(1)

        candidate_option = driver.find_element_by_xpath('//html//li[2]')
        candidate_option.click()
        time.sleep(1)

        first_row = driver.find_element_by_xpath("//html//div[1]/div[1]/div/a/span[1]/span[1]")
        second_row = driver.find_element_by_xpath("//html//div[2]/div[1]/div/a/span[1]/span[1]")
        third_row = driver.find_element_by_xpath("//html//div[3]/div[1]/div/a/span[1]/span[1]")
        fourth_row = driver.find_element_by_xpath("//html//div[4]/div[1]/div/a/span[1]/span[1]")
        fifth_row = driver.find_element_by_xpath("//html//div[5]/div[1]/div/a/span[1]/span[1]")

        sort_filter = driver.find_element_by_tag_name('option')
        sort_filter.click()
        time.sleep(1)

        name_filter = driver.find_element_by_xpath("//option[@value='name']")
        name_filter.click()




sorting = CandidatesList()
sorting.sortby_name()
