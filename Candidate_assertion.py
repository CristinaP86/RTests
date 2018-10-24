from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


class VerifyCandidate:
    def open_correct_candidate(self):
        baseurl = 'https://candidx.io/'
        driver = webdriver.Chrome()
        # options.add_argument('--disable-extensions')
        # options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
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

        candidate_assertion_name = driver.find_element_by_xpath('//html//div[1]/div[1]/div/a/span[1]/span[1]').text
        candidate_assertion_last = driver.find_element_by_xpath('//html//div[1]/div[1]/div/a//span[1]/span[2]').text
        candidate_assertion_name.upper()
        candidate_assertion_last.upper()
        # print(candidate_assertion_name.upper())
        # print(candidate_assertion_last.upper())
        candidate_upper_name = candidate_assertion_name.upper()
        candidate_upper_last = candidate_assertion_last.upper()

        candidate_click = driver.find_element_by_xpath('//html//div[1]/div[1]/div/a')
        candidate_click.click()
        time.sleep(2)

        assert candidate_upper_name in driver.find_element_by_xpath("//span[@class='candid-title']").text
        assert candidate_upper_last in driver.find_element_by_xpath("//span[@class='candid-title']").text

asserting_candidate = VerifyCandidate()
asserting_candidate.open_correct_candidate()
